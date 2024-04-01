import httpx
import json
from datetime import datetime
from multiprocessing import Process

# --- FAST API ---#
from fastapi import Response
from fastapi import FastAPI

# --- settings --- #
from settings import *

app = FastAPI()

#-------------- ROOT ---------------------#
@app.get("/home")
async def root():

    return {"message": "Welcome to the FastAPI application"}
#-----------------------------------------#


async def request(url, header):
    r = httpx.get(url,headers=header)
    return r.json()

#-------------- Crawler ---------------------#


@app.get('/user')
async def start_requests(Github_ID: str):
    token = get_github_token()
    GithubID = Github_ID
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url= f'{API_URL}/users/{GithubID}'
    result = await request(url,headers)
    json_str = json.dumps(result, indent=4, default=str)
    student = json.loads(json_str)
    
    user_item = {
        'GithubID': student['login'],
        'Follower_CNT': student['followers'],
        'Following_CNT': student['following'],
        'Public_repos_CNT': student['public_repos'],
        'Github_profile_Create_Date': student['created_at'],
        'Github_profile_Update_Date': student['updated_at'],
        #'email': student['email'],
        # 'Crawled_Date': datetime.now().strftime("%Y%m%d_%H%M%S")
    }

    return user_item

@app.get('/repo')
async def start_requests():
    token = get_github_token()
    
    GithubID = 'kdgyun'
    repoNM = 'k8s-cluster-bootstrap'

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url= f'{API_URL}/repos/{GithubID}/{repoNM}'

    result = await request(url,headers)
    json_str = json.dumps(result, indent=4, default=str)
    repo = json.loads(json_str)
    
    repo_item = {

        'RepoID' : repo['id'],
        'RepoURL' : repo['html_url'],
        'RepoNM' : repo['name'],
        'OwnerGithubID' : repo['owner']['login'],
        'CreationDate' : repo['created_at'],
        'ForkCount' : repo['forks_count'],
        'StarCount' : repo['stargazers_count'],
        'OpenIssueCount' : repo['open_issues_count'],
        'LicenseName' : repo['license'],
        'ProjectDescription' : repo['description'],
        'ProgrammingLanguage' : None,
        'Contributors' : None,
        'CommitCount' : None,
        'HasReadME' : None,
        'ReleaseVersion' : None
    }   

    return repo_item
