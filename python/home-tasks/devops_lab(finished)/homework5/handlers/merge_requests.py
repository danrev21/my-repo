"""Write your code here"""
import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_merge_requests(state=None):
    if state == "opened" or state == "closed":
        payload = {"state": state, "per_page": "100"}
        request = requests.get("https://git.epam.com/api/v4/projects/124721/merge_requests",
                               params=payload,
                               headers=HEADERS)
        resp_js = request.json()
        merge_table = []
        for i in range(len(resp_js)):
            merge_table.append({"title": resp_js[i]["title"],
                                "num": resp_js[i]["iid"], "link": resp_js[i]["web_url"]})
        return merge_table
    elif state is None:
        payload = {"state": "all", "per_page": "100"}
        request = requests.get('https://git.epam.com/api/v4/projects/124721/merge_requests',
                               params=payload,
                               headers=HEADERS)
        merge_table = []
        resp_js = request.json()
        for i in range(len(resp_js)):
            merge_table.append({"title": resp_js[i]["title"], "num": int(resp_js[i]["iid"]),
                                "link": resp_js[i]["web_url"]})
        return merge_table

    elif state == "verified" or state == "needs work":
        payload = {"state": "opened", "per_page": "100"}
        request = requests.get("https://git.epam.com/api/v4/projects/124721/merge_requests",
                               params=payload,
                               headers=HEADERS)
        resp_js = request.json()
        merge_table = []
        for i in range(len(resp_js)):
            merge_str = "https://git.epam.com/api/v4/projects/124721/merge_requests/"
            pipe_str = str(resp_js[i]["iid"]) + "/pipelines"
            ver_need_str = merge_str + pipe_str
            p_stat_req = requests.get(ver_need_str, params=payload, headers=HEADERS)
            p_stat_js = p_stat_req.json()
            tot_ids = 0
            for n in range(len(p_stat_js)):
                if p_stat_js[n]["id"] > tot_ids:
                    pipe_status = p_stat_js[n]["status"]
                    tot_ids = p_stat_js[n]["id"]
            if pipe_status == "success" and state == "verified":
                merge_table.append({"title": resp_js[i]["title"],
                                    "num": resp_js[i]["iid"], "link": resp_js[i]["web_url"]})
            if pipe_status != "success" and state == "needs work":
                merge_table.append({"title": resp_js[i]["title"],
                                    "num": resp_js[i]["iid"], "link": resp_js[i]["web_url"]})
    return merge_table


if __name__ == "__main__":
    print(get_merge_requests())
