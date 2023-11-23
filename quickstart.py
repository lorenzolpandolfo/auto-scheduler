import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main(tk, msgbox, output):
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

  # Se existir o arquivo do usuário
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      try:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
      )
      except FileNotFoundError as err:
        msgbox.showerror("Erro", f"O arquivo credentials.json não foi encontrado. Insira-o no diretório local.")
        exit()
      
      creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    
    output.insert(tk.END, "Carregando eventos do Google Agenda...\n")

    agora = datetime.datetime.now()
    fuso_horario = datetime.timezone.utc

    inicio_dia = datetime.datetime(agora.year, agora.month, agora.day, 0, 0, 0, tzinfo=fuso_horario)
    fim_dia = datetime.datetime(agora.year, agora.month, agora.day, 23, 59, 59, tzinfo=fuso_horario)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=inicio_dia.isoformat(),
            timeMax=fim_dia.isoformat(),
            maxResults=100,
            singleEvents=True,
            orderBy="startTime"
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("[X] Não foram encontrados eventos para hoje.")
      return

    return events

  except HttpError as error:
    msgbox.showerror("Erro", f"{str(err)}\nTente excluír o arquivo token.json no diretório local.")


if __name__ == "__main__":
  main()