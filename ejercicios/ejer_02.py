# 29 flujos en python
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = [
    "Local Bear Eaten by Man",
    "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree",
    "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic"
]

news_ticker = ""
newHeadLine = True
# write your loop here
for headline in headlines:
    aux = news_ticker
    aux += headline
    if len(aux) > 140:
        newLine = True
        for word in headline:
            if len(news_ticker) < 140:
                if newLine:
                    newLine = False
                    news_ticker += " " + word
                else:
                    news_ticker += word
            else:
                break
    else:
        if newHeadLine:
            newHeadLine = False
            news_ticker += headline
        else:
            news_ticker += " "+headline
print(news_ticker)
