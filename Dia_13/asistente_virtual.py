# instalar yendo a File - Settings - Python interpreter - +
# pyttsx3, speechRecognition, pywhatkit, yfinance, pyjokes
# pip install PyAudio
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


dias_semana = {0:'Lunes',1:'Martes',2:'Miércoles',3:'Jueves',4:'Viernes',5:'Sábado',6:'Domingo'}
meses = ['','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que puede comenzar a grabar
        print('Ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language='es-ar')
            # prueba de que pudo ingresar
            print('Dijiste: ' + pedido)
            # devolver pedido
            return pedido

        except sr.UnknownValueError:
            print('no entendí, intenta de nuevo')
            return 'sigo esperando'

        except sr.RequestError:
            print('el servicio no está disponible')
            return 'sigo esperando'

        except:
            print('algo salió mal')
            return 'sigo esperando'

# para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    id_voice = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    engine.setProperty('voice',id_voice)

    engine.say(mensaje)
    engine.runAndWait()

def informar_dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()

    hablar(f'Hoy es {dias_semana[dia_semana]} {dia.day} de {meses[dia.month]} de {dia.year}')

def informar_hora():
    ahora = datetime.datetime.now()
    hablar(f'Son las {ahora.hour} horas con {ahora.minute} minutos y {ahora.second} segundos')

def saludo_inicial():
    hablar('Hola. Soy tu asistente virtual. ¿En qué puedo ayudarte?')

def pedir_cosas():

    saludo_inicial()
    comenzar = True
    while comenzar:

        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif any(phrase in pedido for phrase in ['abrir navegador', 'abrir google', 'ir a google']):
            print('Entra ' + pedido)
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue

        elif 'salir' in pedido:
            comenzar = False
            continue


pedir_cosas()

# obtener voces del sistema
# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#    print(voice)
