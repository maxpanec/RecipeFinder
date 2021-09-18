import requests
from bs4 import BeautifulSoup


def scrape_allrecipes(url, stop, max_recipes):
    if stop == "0":
        return None
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = [soup.find(class_='component card card__recipe card__facetedSearchResult')]
    recipes = []
    if results[0] is None:
        return None
    for x in range(int(max_recipes)-1):
        temp = results[x].find_next_sibling(class_='component card card__recipe card__facetedSearchResult')
        if temp is not None:
            results.append(temp)
        else:
            break

    for result in results:
        recipeInfo = {}
        start = result.find(class_='card__titleLink manual-link-behavior')
        recipeInfo['name'] = start['title']
        recipeInfo['link'] = start['href']
        temp = result.find(class_='review-star-text')
        if temp is None:
            temp = results[len(results)-1].find_next_sibling(class_='component card card__recipe card__facetedSearchResult')
            if temp is not None:
                results.append(temp)
                continue
            else:
                break
        recipeInfo['stars'] = temp.text.lstrip('Rating: ').rstrip(' stars')
        recipes.append(recipeInfo)
    return recipes

def scrape_epicurious(url, stop, max_recipes):
    if stop == "0":
        return None
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = [soup.find(class_='recipe-content-card')]
    recipes = []
    if results[0] is None:
        return None
    for x in range(int(max_recipes)-1):
        temp = results[x].find_next_sibling(class_='recipe-content-card')
        if temp is not None:
            results.append(temp)
        else:
            break

    for result in results:
        recipeInfo = {}
        name = result.find(class_='controls').find_next()
        recipeInfo['name'] = name['title']
        recipeInfo['link'] = 'https://www.epicurious.com/' + name['href']
        rating = result.find(class_='recipes-ratings-summary')
        stars = rating.find_next(class_='rating')['data-rating']
        if(stars != 'unrated'):
            stars = float(stars) / 4 * 5
        else:
            stars = 0
        recipeInfo['stars'] = stars
        recipes.append(recipeInfo)
    return recipes


def scrape_bonappetit(url, stop, max_recipes):
    if stop == "0":
        return None
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = [soup.find(class_='recipe-content-card')]
    recipes = []
    if results[0] is None:
        return None
    for x in range(int(max_recipes)-1):
        temp = results[x].find_next_sibling(class_='recipe-content-card')
        if temp is not None:
            results.append(temp)
        else:
            break

    for result in results:
        recipeInfo = {}
        start = result.find(class_='hed')
        name = start.next
        recipeInfo['name'] = name.contents[0]
        recipeInfo['link'] = 'https://www.bonappetit.com/' + name['href']
        ratings = start.find_next_sibling(class_='ratings__component').next.children
        stars = 0
        for rating in ratings:
            if rating.next['alt'] == 'Filled star icon':
                stars += 1
        recipeInfo['stars'] = stars
        recipes.append(recipeInfo)
    return recipes

def scrape_foodnetwork(url, stop, max_recipes):
    if stop == "0":
        return None
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = [soup.find(class_='o-RecipeResult o-ResultCard')]
    recipes = []
    if results[0] is None:
        return None
    for x in range(int(max_recipes)-1):
        temp = results[x].find_next_sibling(class_='o-RecipeResult o-ResultCard')
        if temp is not None:
            results.append(temp)
        else:
            break

    for result in results:
        recipeInfo = {}
        start = result.find(class_='m-MediaBlock__a-Headline')
        name = start.find_next()
        recipeInfo['link'] = 'https:' + name['href']
        recipeInfo['name'] = name.next.text
        temp = start.find_next_sibling(
            class_='m-MediaBlock__m-Rating')
        if temp is None:
            continue
        recipeInfo['stars'] = temp.find_next(class_='gig-rating-stars')['title'][0:1]
        recipes.append(recipeInfo)
    return recipes