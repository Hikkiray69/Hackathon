import os
import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print(f'Вы сказали: {text}')
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
        except sr.RequestError as e:
            print(f"Ошибка запроса к сервису распознавания: {e}")
            return None

def recognize_speech_from_wav(file_path):
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return None

    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print(f'Распознанный текст: {text}')
            return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь в аудиофайле")
            return None
        except sr.RequestError as e:
            print(f"Ошибка запроса к сервису распознавания: {e}")
            return None

def handle_intent(text):
    print(f"Обработанный текст: {text}")  # Для отладки
    text = text.lower().strip()
    if "изменения тарифа" in text:
        print("Вызов функции F12")
        function_F12()
    elif "подключение услуги" in text:
        print("Вызов функции F23")
        function_F23()
    elif "заключение договора" in text:
        print("Вызов функции F34")

def function_F12():
    print("Выполняется функция F12")

def function_F23():
    print("Выполняется функция F23")

def function_F34():
    print("Выполняется функция F34")

if __name__ == '__main__':
    # Распознавание из микрофона
    mic_text = recognize_speech_from_mic()
    print(f"Распознанный текст из микрофона: {mic_text}")  # Для отладки
    if mic_text:
        handle_intent(mic_text)
    
    # Распознавание из WAV файла
    wav_file_path = 'output1.wav'  # Укажите путь к вашему WAV файлу
    wav_text = recognize_speech_from_wav(wav_file_path)
    if wav_text:
        handle_intent(wav_text)