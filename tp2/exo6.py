import requests

def get_university_data(country="France"):
    url = f"http://universities.hipolabs.com/search?country={country}"
    rawdata = requests.get(url)
    if not rawdata:
        raise Exception
    data = rawdata.json()
    return data
if __name__ == "__main__":
    uni_data = get_university_data("France")
    uni_filtrees = []
    for uni in uni_data:
        if uni["state-province"] is not None:
            uni_filtrees.append(uni)
    uni_filtrees.sort(key=lambda u: u["state-province"])
    for uni in uni_filtrees:
        nom = uni["name"]
        etat = uni["state-province"]
        site = uni["web_pages"][0] if uni["web_pages"] else "Pas de site"
        print(f"Université : {nom}")
        print(f"  Région/État : {etat}")
        print(f"  Site web    : {site}")
        print("-" * 30)