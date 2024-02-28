json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            
            t.config(text=(temp,"°"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
            
            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)