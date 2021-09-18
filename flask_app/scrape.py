import flask_app.scapefunctions as scapefunctions

def scrapeInfo(search_data):
    search = search_data['search']
    allrecipes_url = "https://www.allrecipes.com/search/results/?search=" + search.replace(' ', '+')
    epicurious_url = "https://www.epicurious.com/search/" + search.replace(' ', '%20') + "?sort=mostReviewed"
    bonappetit_url = "https://www.bonappetit.com/search/" + search.replace(' ', '%20') + "?content=recipe&sort=mostReviewed"
    foodnetwork_url = "https://www.foodnetwork.com/search/" + search.replace(' ', '-') + "-"

    total_recipes = {
        'allrecipes': scapefunctions.scrape_allrecipes(allrecipes_url, search_data['allrecipes'], search_data['range']),
        'epicurious': scapefunctions.scrape_epicurious(epicurious_url, search_data['epicurious'], search_data['range']),
        'bonappetit': scapefunctions.scrape_bonappetit(bonappetit_url, search_data['bonappetit'], search_data['range']),
        'foodnetwork': scapefunctions.scrape_foodnetwork(foodnetwork_url, search_data['foodnetwork'], search_data['range'])
    }
    return total_recipes