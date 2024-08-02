## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

# Import Important libraries
import streamlit as st
import google.generativeai as genai
import os

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the Model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Load Gemini Pro model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


# Navbar
st.set_page_config(
    page_title="Proposal Generator",
    page_icon="👥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "✨ Upwork Proposal Generator ✨"
    "</h1>",
    unsafe_allow_html=True
)

#st.title('✨ AI Blog Section Generator')

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 20px;
    line-height: 0px;
    margin-top: 0;
    margin-bottom: 24px;
    text-align: center;
    display: flex;
    justify-content: center;
}
</style>
<h3 style="text-align: center; color: black; font-weight: 300; font-style: italic;">✨ Powered by AppJingle Solutions ✨</h3>
''', unsafe_allow_html=True)

# sidebar for the user input

with st.sidebar:
    st.markdown(
        "<style>h1 {text-align: center;}</style>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<style>h1 {text-align: center; color: black;}</style>",
        unsafe_allow_html=True
    )
    st.title("Input Settings")

    st.markdown(
        "<style>"
        "h4 {text-align: left; color: black; margin-top: 4px;}"
        "p {text-align: left; color: black;}"
        "</style>",
        unsafe_allow_html=True
    )
    st.markdown("<h4>Enter Details: </h4>", unsafe_allow_html=True)
    
     # Title
    
    name = st.text_input("Name (Your Name)")
    
    # Section Heading
    job_title = st.text_input("Heading (Job Title)")
    
    # Add the Voice Tones
    voice_tones = st.sidebar.selectbox("Speaking Tones:", ["Formal", "Informal", "Friendly", "Bold", "Adventurous", "Witty", "Professional", "Casual", "Informative", "Creative", "Trendy", "Caring", "Cheerful", "Excited", "Funny", "Sad", "Serious", "Tense", "Vulnerable", "Angry", "Surprised", "Worried", "Assertive", "Confident", "Cooperative", "Encouraging" ])
    
    # Add the Writing Styles
    writing_styles = st.sidebar.selectbox("Choose Writing Styles:", ["Academic", "Conversational", "Creative", "Critical", "Descriptive", "Instructive", "Technical", "Analytical","Business", "Causal", "Emotional", "Expository", "Formal", "Informal", "Legal", "Medical", "Poetic", "Persuasive"])
    
    # Audience
    #audience = st.selectbox("Audience: Who is the target audience?", ["Teenager", "Adult", "20-years-old", "30-years-old",  "40-years-old", "50-years-old", "Senior", "Everyone", "Uninformed Audience", "Neutral Audience", "Business Audience", "Researcher", "Expert Audience", "My Boss", "My Student", "My Teacher", "My Family", "My Friends", "My Colleagues"] )
    
    # Country
    description = st.text_area("Detail of Job (Description)")
    #num_words = st.number_input("Number of words", min_value=250, max_value=3000, step=50)

    # Primary Keyword
    #primary_keyword = st.text_input("Primary Keyword ")
    
    # Secondary Keyword
    #secondary_keyword = st.text_input("Secondary Keyword")
    
    # Reference Article Link
    # reference_article_link = st.text_input("Reference Article Link")

    # Prompt
    prompt_parts = [
        
            f""" 
            Your name is {name}, you are the most successful freelancer on Upwork. You make proposals to work on jobs that others have posted on Upwork and always get chosen by the job poster in a tough competition. You write such a great proposal that it always gets selected out of the other 50 proposals.

                Here are some essential points to note while writing an Upwork proposal:
                - Writing an Upwork proposal requires skill and practice.
                - A good proposal should have a clear structure and include common elements.
                - The proposal should start with a greeting and introduction, then a restatement of the client's core need.
                - It should include a statement that demonstrates your ability to solve the problem and start immediately.
                - A short pitch should highlight why you are the right fit for the job.
                - The proposal should describe the methods and processes you will use to approach the project.
                - Attachments such as relevant documents, sample works, or portfolio links should be included.
                - The proposal should be brief, clean, and concise, typically consisting of three short paragraphs.
                - Attention-grabbing sentences are essential to prevent your proposal from being ignored.
                - Showing an understanding of the client's goals and job description is crucial.
                - Providing proof of past experience and work samples builds trust and credibility.
                - Asking relevant questions and offering solutions shows your qualifications.
                - Finding ways to stand out from competitors, such as using an introductory video, can be effective.
                - The proposal should highlight the reasons why the client should choose you.
                - Avoid using proposal templates and instead personalize each proposal to the specific project.
                - Focus on the client's needs and problems rather than talking too much about yourself.
                - Avoid unnecessary details and keep the proposal concise and impactful.
                - Strike a balance between being professional and personable in your writing.
                - Avoid being too casual or overly formal in your tone.
                - Find the middle ground to connect with the client effectively and leave a positive impression.


                Here are some example proposals:

                Upwork proposal example #1:

                Hi,

                I would love to be your freelance writer and help you execute your website content strategy.

                I have 5 years of experience writing content for websites, including Forbes.com, Buzzfeed.com, and more. Below, I've linked two samples that showcase my writing ability in a similar niche to your brand. As you can see, I understand your audience and know how to write compelling articles to get your website visitors to purchase your products.

                I can complete 1,000-word articles with a 2-day turnaround time. Would that work for your needs? Let me know if my writing meets your expectations, and we can set up a time to talk about your project in more detail.

                Example Website Content #1 (link)

                Example Website Content #2 (link)

                Thanks,
                {name}

                ---

                Upwork proposal example #2:

                Hello,

                If you need high-quality articles written for your website at an affordable price, I am the right writer for you! My goal with every content piece is to lead your website's visitors along their buyer's journey—hopefully ending with a purchase on your website.

                As you can see in my Upwork profile, I have three years of experience writing content for websites just like yours. You can even find some of my published work on Inc.com, Marketwatch.com, and Hubspot.com. Linked below are two writing samples that demonstrate my ability to craft excellent blog content for B2B e-commerce websites.

                - Example Website Article #1

                - Example Website Article #2

                My current turnaround time for 1,000-word articles is two days. If my work aligns with what you need, can we set up a time to discuss your goals for this project?

                Best regards,
                {name}

                ---

                Upwork proposal example #3:

                Hello Nicki,

                I'm a detail-driven writer who turns ideas into valuable website content for clients just like you. I enjoy writing for various topics and niches (business, lifestyle, travel, personal blogs, etc.). You can find examples of my past writing work on my Upwork profile, plus (insert link here) and (insert link here).

                My experience has given me a deep understanding of SEO writing and strong digital marketing strategies to help drive traffic to your site. I excel in writing all types of content such as blogs, press releases, product descriptions, and more.

                My rate is $50 for projects like this one, and I can have a finished piece of writing delivered to you this week if you're interested. Let's talk!

                - {name}


                I will give you a job title, description and you have to write the best proposal possible to work on that job, using all the information that is given above. The proposal should be extremely short and little and contains only 2 paragraphs. Write like a human. Avoided passive constructs and select words that convey your message effectively without being overly complex. Please write in English language. You have a {voice_tones} tone of voice. You have a {writing_styles} writing style. Don't use jargon and complex terms like showcase, leverage, delve, craft, dig, dive etc. Don't use words like excited, understand, dive, knack, seasoned, post, thrilled, eager, crafting, proficient etc. Don't use this sentence: i saw your post, I'm eager. Please sign off the letter using the name Farhan Akbar.

                Here is The job title is {job_title}.

                The following is the job description:
                {description} 
                
                Please ignore all previous instructions. I want you to respond only in English. I want you to act as a very proficient Professional Freelancer and a great problem solver that speaks and writes fluent English. I want you to pretend that you know how to win a job on Upwork very well and you are a professional in this work.
            Writing some catchy first few lines is vital to ensuring your proposal doesn't get ignored. Clients can only see the first two lines of your proposal unless they click to expand it, so you have to write something compelling if you want to stand out. Let the employer know how you will complete the job. The first few sentences should confirm that you fully understand what the client needs. Your proposal doesn't need to be lengthy as long as it confirms you understand the problem and shows that you can solve it. Always aim for brief, clean, and concise writing. Typically, everything you need can be expressed in three short paragraphs.
            Here is The job title is {job_title}.
            Here is the full text of the job listing: {description}.
            Here is the instructions:
            1. So write it to follow this format: Solutions (First paragraph).
            2. Tools (Second paragraph)
            3. Soft skills + availability (Third paragraph)
            4. Invitation to a meeting (Call to action)
            6. Write like a human. Avoided passive constructs and select words that convey your message effectively without being overly complex.
            7. You have a {voice_tones} tone of voice. You have a {writing_styles} writing style.
            8. Don't use jargon and complex terms like showcase, leverage, delve, craft etc.
            9. Focus first on creating high quality, thorough content that provides value to readers.
            10. Keep Your Paragraphs Short: Aim for about five sentences per paragraph. This helps in maintaining a clear and concise structure, making it easier for readers to follow.
            11. Choose Your Words Carefully: Utilize action words to keep the narrative dynamic and engaging. Avoid passive constructs and select words that convey your message effectively without being overly complex.
            12. Shorten Your Sentences: Restrict sentence length to 10-15 words. This simplifies the information and aids comprehension. Avoid lengthy sentences that could confuse or deter your audience.
            13. Keep it Simple: Use straightforward language. Opt for simpler words when possible (e.g., use "small" instead of "minuscule"). This prevents the text from being pretentious and maintains the reader's focus.
            14. Break it Up: Organize your content into digestible sections. Use headings and subheadings to divide text and guide the reader through your article. Consider splitting complex topics into multiple posts or a series for easier consumption and sustained engagement.
            15. Write for Your Audience, Not for Your Score: Always prioritize your reader's needs and interests over adhering strictly to readability scores or SEO guidelines. If the content requires complexity for clarity or depth, adjust your style accordingly.
            16. Write in simple easy to read tone, use simple language aim for a readability score of grade 8.
            17. Do not echo my prompt. Do not remind me what I asked you for. Do not apologize. Do not self-reference. Do not use generic filler phrases. Get to the point precisely and accurate.
            18. Follow this example pattern and also the wording like written below: 
               
               Solutions

                Hi Harvey,
                I can help you with boosting your sales and brand awareness. I will study your business model and market to create campaigns accurately. My strategy would increase your ROI significantly.

                Tools

                I will create a landing page if you still need one. I would be designing creatives using Canva and Photoshop and writing captions that would be appealing and drive traffic to the landing pages.

                Soft skills + availability

                I could work well with the team as well as independently. I will be following your team's SOPs. I have an eye for detail and could come up with productive ideas.

                Invitation to a meeting

                We can schedule a meeting to discuss the project details.
         
         
         Please write the proposal strictly according to above instructions and examples mentioned above. Please make the 5 variations of the proposal with mix of Upwork proposal styles and tones and examples. Write like a proficient Professional Freelancer and a great problem solver that speaks and writes fluent English.
            """

            ]
            

    # Submit Button
    submit_button = st.button("Generate")

if submit_button:
    # Display the spinner
    with st.spinner("Generating...."):
        # Generate the response
        response = model.generate_content(prompt_parts)
        # Write results
        st.write(response.text)

    # Add styling to the generated text
    st.markdown('''
        <style>
            p {
                font-family: 'Open Sans', sans-serif;
                font-size: 16px;
                line-height: 24px;
                margin-top: 0;
                margin-bottom: 24px;
            }
            strong {
                font-weight: 600;
            }
            em {
                font-style: italic;
            }
            code {
                background-color: #f5f5f5;
                border-radius: 3px;
                display: inline-block;
                font-family: 'Menlo', monospace;
                font-size: 14px;
                margin: 0 1px;
                padding: 2px 4px;
            }
        </style>
    ''', unsafe_allow_html=True)

clear_button = st.sidebar.button("Clear All")
with st.sidebar:
    st.markdown('''
        <style>
            .element-container .stButton.stBtn {
                background-color: #ffc107 !important;
                border-color: #ffc107 !important;
            }
        </style>
    ''', unsafe_allow_html=True)

    if clear_button:
        for key in st.session_state:
            if isinstance(st.session_state[key], str) and st.session_state[key] != "":
                st.session_state[key] = ""
            elif isinstance(st.session_state[key], list) and st.session_state[key] != []:
                st.session_state[key] = []
            elif isinstance(st.session_state[key], dict) and st.session_state[key] != {}:
                st.session_state[key] = {}


# Adding the HTML footer
# Profile footer HTML for sidebar


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923034532403"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="https://www.facebook.com/appjingle"><img src="https://img.shields.io/badge/Facebook-Connect-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True) 


      
        
        

        

