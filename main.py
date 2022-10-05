import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
response1 = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
rawname = response.json()[0]['name_with_namespace']

print(f"\n\n\n GitLub Projects of    {rawname.split('/')[0]}   Are Listed below  ")

print("\n\n")

all_projects = response.json()
for project in all_projects:
    print(f"Project Name: {project['name']} Project Url: {project['web_url']}")
