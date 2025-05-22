import python_weather
import asyncio
import os


try:
    async def getweather():
        async with python_weather.Client(format=python_weather.IMPERIAL) as client:
            print()
            input2 = input('FOR WHICH LOCATION YOU WOULD LIKE TO KNOW THE WEATHER CONDITION: ').lower()
            print()
            weather = await client.get(input2)
            temperature = weather.current.temperature
            print("THE TEMPERATURE IN", input2.upper(), "IS: ", str(temperature) + ' F')
            print()
            for forecast in weather.forecasts:
                print("THE PRESENT TIME IN", input2.upper(), "IS: ", forecast.date)
                print()
                ast = str(forecast.astronomy)
                ast = ast.replace('<', '')
                ast = ast.replace('>', '')
                ast = ast.strip()
                ast = ast.split()
                ast.pop(0)
                ast = tuple(ast)
                for i in ast:
                    i = i.replace('_', ' ')
                    i = i.replace('=', ' = ')
                    i = i.replace('datetime.time(', '')
                    i = i.replace(')', '')
                    i = i.replace(',', ' : ')
                    i = i.upper()
                    if 'SUN' in i:
                        print(i, end='')
                    else:
                        print(i)
                break

            for forecast in weather.forecasts:
                for hourly in forecast.hourly:
                    type = str(hourly)
                    type = type.split()
                    type.pop(0)
                    type.pop(0)
                    type.pop(0)
                    temp = ''
                    for i in type:
                        i = i.replace('=', ' = ')
                        i = i.replace('️>', '')
                        i = i.replace("'", '')
                        i = i.upper()
                        i = i.strip()
                        i = i + '   '
                        temp = temp + i
                    temp = temp.strip()
                    print(temp)
                    break
                break
except:
    pass



if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(getweather())