# # import requests
# # import pandas as pd
# # import time
# # import re

# # HUNTER_API_KEY = "e7f6461d322b8decb7307d59abe4cbc5b7a627e1"

# # def get_company_domain(linkedin_url):
# #     try:
# #         name = re.search(r'company/([^/]+)', linkedin_url).group(1)
# #         name = name.replace('-', '')
# #         return name + ".com"
# #     except:
# #         return None

# # def find_emails(domain):
# #     url = "https://api.hunter.io/v2/domain-search"
# #     params = {
# #         "domain": domain,
# #         "api_key": HUNTER_API_KEY
# #     }

# #     response = requests.get(url, params=params)

# #     if response.status_code == 200:
# #         data = response.json()["data"]["emails"]
# #         return [email["value"] for email in data]
# #     else:
# #         print("Error:", response.status_code)
# #         return []

# # df = pd.read_csv("input.csv")

# # results = []

# # for index, row in df.iterrows():
# #     domain = get_company_domain(row["linkedin_url"])
    
# #     if domain:
# #         emails = find_emails(domain)
        
# #         for email in emails:
# #             results.append({
# #                 "company": row["company_name"],
# #                 "linkedin": row["linkedin_url"],
# #                 "domain": domain,
# #                 "email": email
# #             })

# #     time.sleep(5)

# # pd.DataFrame(results).to_csv("output.csv", index=False)
# # print("Done. Check output.csv")

# import streamlit as st
# import requests
# import re
# import pandas as pd
# import time

# HUNTER_API_KEY = "e7f6461d322b8decb7307d59abe4cbc5b7a627e1"

# def get_company_domain(linkedin_url):
#     try:
#         name = re.search(r'company/([^/]+)', linkedin_url).group(1)
#         name = name.replace('-', '')
#         return name + ".com"
#     except:
#         return None

# def find_emails(domain):
#     url = "https://api.hunter.io/v2/domain-search"
#     params = {
#         "domain": domain,
#         "api_key": HUNTER_API_KEY
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()["data"]["emails"]
#         return [email["value"] for email in data]
#     else:
#         return []

# st.title("LinkedIn Company Email Finder")

# url = st.text_input("Enter LinkedIn Company URL")

# if st.button("Find Emails"):
#     if url:
#         domain = get_company_domain(url)
        
#         if domain:
#             st.write("Company Domain:", domain)
#             emails = find_emails(domain)
            
#             if emails:
#                 st.write("Emails Found:")
#                 for email in emails:
#                     st.write(email)
#             else:
#                 st.write("No emails found.")
#         else:
#             st.write("Invalid LinkedIn URL")

#     st.subheader("Upload CSV")
# uploaded_file = st.file_uploader("Upload CSV with LinkedIn URLs", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write([repr(col) for col in df.columns])
#     results = []
    

#     for index, row in df.iterrows():
#         domain = get_company_domain(row["linkedin_url"])
#         if domain:
#             emails = find_emails(domain)
#             for email in emails:
#                 results.append({
#                     "company": row["company_name"],
#                     "domain": domain,
#                     "email": email
#                 })
#         time.sleep(2)

#     result_df = pd.DataFrame(results)
#     st.write(result_df)
#     result_df.to_csv("output.csv", index=False)





























# import streamlit as st
# import requests
# import re
# import pandas as pd
# import time
# import urllib.parse
# import base64

# HUNTER_API_KEY = "e7f6461d322b8decb7307d59abe4cbc5b7a627e1"

# # -------- Background Image --------
# def add_bg_from_local():
#     with open("bg_photo.jpeg", "rb") as image_file:
#         encoded = base64.b64encode(image_file.read()).decode()

#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: url("data:image/jpg;base64,{encoded}");
#             background-size: cover;
#             background-attachment: fixed;
#         }}

#         h1, h2, h3, h4, h5, h6, p, label {{
#             color: white !important;
#         }}

#         .card {{
#             background-color: rgba(0,0,0,0.6);
#             padding: 20px;
#             border-radius: 15px;
#             margin-bottom: 15px;
#             box-shadow: 0 4px 10px rgba(0,0,0,0.5);
#         }}

#         .email-text {{
#             font-size: 18px;
#             font-weight: bold;
#             color: #00FFCC;
#         }}

#         .stButton>button {{
#             background-color: #00C9A7;
#             color: white;
#             border-radius: 10px;
#             height: 2.5em;
#             width: 200px;
#             font-size: 16px;
#         }}

#         .stTextInput>div>div>input {{
#             background-color: rgba(255,255,255,0.9);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_from_local()

# # -------- Functions --------
# def get_company_domain(linkedin_url):
#     try:
#         name = re.search(r'company/([^/]+)', linkedin_url).group(1)
#         name = name.replace('-', '')
#         return name + ".com"
#     except:
#         return None

# def find_emails(domain):
#     url = "https://api.hunter.io/v2/domain-search"
#     params = {
#         "domain": domain,
#         "api_key": HUNTER_API_KEY
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()["data"]["emails"]
#         return [email["value"] for email in data]
#     else:
#         return []

# def generate_email_template(company):
#     subject = f"Quick question about {company}"

#     body = (
#         f"Hi,\n\n"
#         f"I wanted to reach out to see if {company} works with external development partners for web or software development.\n\n"
#         f"My team helps companies with web development, CRM systems and custom software.\n\n"
#         f"If this is relevant, I’d love to connect for a quick discussion.\n\n"
#         f"Best regards,\n"
#         f"Lingesh\n"
#         f"Icebergs Tech"
#     )

#     return subject, body

# # -------- UI --------
# st.title("Foreign Client Email Finder")

# url = st.text_input("Enter LinkedIn Company URL")

# if st.button("Find Emails"):
#     if url:
#         domain = get_company_domain(url)
        
#         if domain:
#             st.success(f"Company Domain: {domain}")
#             emails = find_emails(domain)
            
#             if emails:
#                 st.subheader("Emails Found")

#                 for email in emails:
#                     subject, body = generate_email_template(domain)

#                     subject_encoded = urllib.parse.quote(subject)
#                     body_encoded = urllib.parse.quote(body)

#                     gmail_link = f"https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to={email}&su={subject_encoded}&body={body_encoded}"

#                     st.markdown(f"""
#                     <div class="card">
#                         <div class="email-text">{email}</div>
#                         <br>
#                         <a href="{gmail_link}" target="_blank">
#                             <button>Send Email</button>
#                         </a>
#                     </div>
#                     """, unsafe_allow_html=True)

#             else:
#                 st.error("No emails found.")
#         else:
#             st.error("Invalid LinkedIn URL")

# # -------- CSV Upload --------
# st.subheader("Upload CSV")
# uploaded_file = st.file_uploader("Upload CSV with LinkedIn URLs", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     results = []
    
#     for index, row in df.iterrows():
#         domain = get_company_domain(row["linkedin_url"])
#         if domain:
#             emails = find_emails(domain)
#             for email in emails:
#                 results.append({
#                     "company": row["company_name"],
#                     "domain": domain,
#                     "email": email
#                 })
#         time.sleep(2)

#     result_df = pd.DataFrame(results)
#     st.write(result_df)

#     st.subheader("Send Emails")
#     for index, row in result_df.iterrows():
#         subject, body = generate_email_template(row["company"])

#         subject_encoded = urllib.parse.quote(subject)
#         body_encoded = urllib.parse.quote(body)

#         gmail_link = f"https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to={row['email']}&su={subject_encoded}&body={body_encoded}"

#         st.markdown(f"""
#         <div class="card">
#             <div class="email-text">{row['email']}</div>
#             <br>
#             <a href="{gmail_link}" target="_blank">
#                 <button>Send Email</button>
#             </a>
#         </div>
#         """, unsafe_allow_html=True)

#     result_df.to_csv("output.csv", index=False)







import streamlit as st
import requests
import re
import pandas as pd
import time
import urllib.parse
import base64

HUNTER_API_KEY = "e7f6461d322b8decb7307d59abe4cbc5b7a627e1"

# -------- Background Image --------
def add_bg_from_local():
    with open("bg_photo.jpeg", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}

        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
        }}

        .card {{
            background-color: rgba(0,0,0,0.65);
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }}

        .email-text {{
            font-size: 18px;
            font-weight: bold;
            color: #00FFCC;
        }}

        .role-text {{
            font-size: 15px;
            color: #FFD700;
        }}

        .stButton>button {{
            background-color: #00C9A7;
            color: white;
            border-radius: 10px;
            height: 2.5em;
            width: 200px;
            font-size: 16px;
        }}

        .stTextInput>div>div>input {{
            background-color: rgba(255,255,255,0.9);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

# -------- Functions --------
def get_company_domain(website_url):
    try:
        website_url = website_url.replace("https://", "").replace("http://", "").replace("www.", "")
        domain = website_url.split("/")[0]
        return domain
    except:
        return None

# -------- Fallback: Scrape emails from website --------
def scrape_emails_from_website(domain):
    emails = set()
    try:
        url = f"http://{domain}"
        response = requests.get(url, timeout=5)
        matches = re.findall(r"[A-Za-z0-9._%+-]+@" + re.escape(domain), response.text)
        for email in matches:
            emails.add(email)
    except:
        pass
    return list(emails)


# -------- Fallback: Generate common emails --------
def generate_common_emails(domain):
    prefixes = ["info", "contact", "hello", "sales", "support", "admin", "careers"]
    return [f"{prefix}@{domain}" for prefix in prefixes]

def find_emails(domain):
    url = "https://api.hunter.io/v2/domain-search"
    params = {
        "domain": domain,
        "api_key": HUNTER_API_KEY
    }

    response = requests.get(url, params=params)
    results = []

    # -------- Hunter Emails --------
    if response.status_code == 200:
        data = response.json()["data"]["emails"]
        for email in data:
            results.append({
                "email": email.get("value", ""),
                "name": (email.get("first_name", "") + " " + email.get("last_name", "")).strip(),
                "role": email.get("position", "Not Available"),
                "linkedin": email.get("linkedin", "")
            })

    # -------- If Hunter fails, use fallback --------
    if not results:
        scraped_emails = scrape_emails_from_website(domain)
        common_emails = generate_common_emails(domain)

        for email in scraped_emails:
            results.append({
                "email": email,
                "name": "",
                "role": "From Website",
                "linkedin": ""
            })

        for email in common_emails:
            results.append({
                "email": email,
                "name": "",
                "role": "Common Email",
                "linkedin": ""
            })

    return results

def generate_email_template(company, name=""):
    subject = f"Exploring Opportunities to Support {company}'s Operational Efficiency"

    body = (
        f"Hi {name if name else ''},\n\n"
        f"I hope you’re doing well.\n\n"
        f"I came across your profile and was impressed by your experience in driving operational efficiency and optimizing business processes within your organization.\n\n"
        f"Your approach to improving workflows and building scalable systems aligns closely with the kind of challenges we help solve.\n\n"
        f"I’m reaching out from IcebergTech. We offer end-to-end IT services and solutions focused on:\n\n"
        f"- Custom software development\n"
        f"- Workflow automation\n"
        f"- Data-driven decision support\n"
        f"- Mobile and web application development\n"
        f"- System integration and process optimization\n\n"
        f"Our solutions are designed to help organizations streamline operations, improve efficiency, and build scalable systems for long-term growth.\n\n"
        f"I would be glad to connect and understand your current requirements to explore how we can support your initiatives. "
        f"Please let me know a convenient time to connect.\n\n"
        f"Looking forward to your response.\n\n"
        f"Best regards,\n"
        f"Lingesh\n"
        f"IcebergTech\n"
        f"Your Number"
    )

    return subject, body
# -------- UI --------
st.title("Client Email Finder")

url = st.text_input("Enter Company website URL")

if st.button("Find Emails"):
    if url:
        domain = get_company_domain(url)
        
        if domain:
            st.success(f"Company Domain: {domain}")
            people = find_emails(domain)
            
            if people:
                st.subheader("Contacts Found")

                for person in people:
                    email = person["email"]
                    name = person["name"]
                    role = person["role"]
                    linkedin = person["linkedin"]

                    subject, body = generate_email_template(domain, name)

                    subject_encoded = urllib.parse.quote(subject)
                    body_encoded = urllib.parse.quote(body)

                    gmail_link = f"https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to={email}&su={subject_encoded}&body={body_encoded}"

                    st.markdown(f"""
                    <div class="card">
                        <div class="email-text">{email}</div>
                        <div style="color:white;">Name: {name}</div>
                        <div class="role-text">Role: {role}</div>
                        <br>
                        <a href="{linkedin}" target="_blank" style="color:#00BFFF;">LinkedIn Profile</a>
                        <br><br>
                        <a href="{gmail_link}" target="_blank">
                            <button>Send Email</button>
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

            else:
                st.error("No emails found.")
        else:
            st.error("Invalid Company URL")

# -------- CSV Upload --------
st.subheader("Upload CSV")
uploaded_file = st.file_uploader("Upload CSV with Company's Website URLs", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []
    
    for index, row in df.iterrows():
        domain = get_company_domain(row["website_url"])
        if domain:
            people = find_emails(domain)
            for person in people:
                results.append({
                    "company": row["company_name"],
                    "email": person["email"],
                    "role": person["role"]
                })
        time.sleep(2)

    result_df = pd.DataFrame(results)
    st.write(result_df)

    st.subheader("Send Emails")
    for index, row in result_df.iterrows():
        subject, body = generate_email_template(row["company"])

        subject_encoded = urllib.parse.quote(subject)
        body_encoded = urllib.parse.quote(body)

        gmail_link = f"https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&to={row['email']}&su={subject_encoded}&body={body_encoded}"

        st.markdown(f"""
        <div class="card">
            <div class="email-text">{row['email']}</div>
            <div class="role-text">Role: {row['role']}</div>
            <br>
            <a href="{gmail_link}" target="_blank">
                <button>Send Email</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    result_df.to_csv("output.csv", index=False)
