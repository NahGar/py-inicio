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
import subprocess
import unicodedata

dias_semana = {0:'Lunes',1:'Martes',2:'Miércoles',3:'Jueves',4:'Viernes',5:'Sábado',6:'Domingo'}
meses = ['','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
cartera = {
    'apple': 'AAPL',
    'amazon': 'AMZN',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'tesla': 'TSLA',
    'meta': 'META',
    'netflix': 'NFLX',
    'nvidia': 'NVDA',
    'twitter': 'TWTR',
    'intel': 'INTC',
    'amd': 'AMD',
    'adobe': 'ADBE',
    'salesforce': 'CRM',
    'oracle': 'ORCL',
    'ibm': 'IBM',
    'cisco': 'CSCO',
    'qualcomm': 'QCOM',
    'paypal': 'PYPL',
    'uber': 'UBER',
    'airbnb': 'ABNB',
    'spotify': 'SPOT',
    'shopify': 'SHOP',
    'snap': 'SNAP',
    'atlassian': 'TEAM',
    'servicenow': 'NOW'
}

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

def normalizar_texto(texto):
    # Quita tildes y convierte a minúsculas
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower()

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

def abrir_calculadora():
    subprocess.Popen("calc")

def pedir_cosas():

    saludo_inicial()
    comenzar = True
    while comenzar:

        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in normalizar_texto(pedido):
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif any(phrase in normalizar_texto(pedido) for phrase in ['abrir navegador', 'abrir google', 'ir a google']):
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue

        elif 'que dia es' in normalizar_texto(pedido) or 'que fecha es' in normalizar_texto(pedido):
            informar_dia()
            continue

        elif 'que hora es' in normalizar_texto(pedido):
            informar_hora()
            continue

        elif 'abrir calculadora' in normalizar_texto(pedido):
            hablar('Muy bien')
            abrir_calculadora()
            continue

        elif 'buscar en wikipedia' in normalizar_texto(pedido):
            hablar('Buscando en wikipedia')
            buscar = pedido.replace('buscar en wikipedia','')
            wikipedia.set_lang('es')
            # sentences es la cantidad de párrafos que devuelve
            resultado = wikipedia.summary(buscar, sentences=3)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue

        elif 'buscar en internet' in normalizar_texto(pedido):
            hablar('Buscando')
            buscar = pedido.replace('buscar en internet','')
            pywhatkit.search(buscar)
            hablar('Esto es lo que he encontrado')
            continue

        elif 'reproducir' in normalizar_texto(pedido):
            hablar('Reproduciendo en youtube')
            buscar = pedido.replace('reproducir','')
            pywhatkit.playonyt(buscar)
            continue

        elif any(phrase in normalizar_texto(pedido) for phrase in ['broma', 'chiste']):
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in normalizar_texto(pedido) or 'precio de la accion' in normalizar_texto(pedido):
            accion = pedido.split('de')[-1].strip()

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de la acción {accion} es {precio_actual}')
            except:
                hablar('Perdón, pero no la he encontrado')
            finally:
                continue

        elif 'salir' in pedido:
            hablar('Hasta luego')
            comenzar = False
            continue


pedir_cosas()

# obtener voces del sistema
# engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#    print(voice)
