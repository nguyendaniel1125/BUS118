from openai import OpenAI
import streamlit as st 
import requests

client = OpenAI(api_key= 'OPEN_API_KEY')
# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are giving advice for flooding information. Please provide ways to prevent, detect, and escape flooding in bullet format using the given zip code."},
        {"role": "user", "content": prompt}
        ]
    )
   return completion.choices[0].message.content

# Downloads an image from the given url.
def download_image(filename, url):
  response = requests.get(url)
  if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
  else:
        print("Error downloading image from URL:", url)

def get_image(prompt, model="dall-e-2"):
  n = 2   # Number of images to generate
  image = client.images.generate(
        prompt= "Flooding in this zip code" + prompt,
        model=model,
        n=n,
        size="1024x1024"
        
    )

  img_url = image.data[0].url
  return img_url



st.title('Enter your zip code')
st.subheader('Local infomation about flooding will be provided')
# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Enter a ZIP Code") # TODO!
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))
        st.image(get_image(prompt))


