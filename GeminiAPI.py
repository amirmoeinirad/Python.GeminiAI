
# Amir Moeini Rad
# November 2025

from google import genai

myApiKey = 'your api key'

client = genai.Client(api_key=myApiKey)

print('\nConnected to Google Gemini API.')

myPrompt = "Explain how AI works in a few words.\n"
print('\nPrompt: ' + myPrompt)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=myPrompt,
)

print('Response: ' + response.text)

print('\nDone.')