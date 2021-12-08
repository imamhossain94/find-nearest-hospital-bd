## Find The Nearest Hospital in BD
* Request by your current location latitude & longitude
* get hospital name, contact number as response

### Calculation
Using Haversine Formula to find the nearest point (e.g. city) based on latitude and longitude.
```
hav(θ) = sin2(θ2).
```

### Law of Haversine:
To derive law of Haversine one needs to start the calculation with spherical law of cosine i.e cos a = cos b * cos c + sin b * sin c * cos A 
One can derive Haversine formula to calculate distance between two as:
```
a = sin²(ΔlatDifference/2) + cos(lat1).cos(lt2).sin²(ΔlonDifference/2)
c = 2.atan2(√a, √(1−a))
d = R.c

where,

ΔlatDifference = lat1 – lat2 (difference of latitude)

ΔlonDifference = lon1 – lon2 (difference of longitude)

R is radius of earth i.e 6371 KM or 3961 miles

and d is the distance computed between two points.
```


### API Endpoint
```html
https://find-nearest-hospital-bd.herokuapp.com/main/v1/loc?lat=23.7869245&lng=90.3774381
```

### API Response
```json
{
  "data": {
    "lat": 23.7763428,
    "lon": 90.3696447,
    "name": "National Institute Of Neurosciences & Hospital",
    "phone": "01726920703"
  },
  "status": "success",
  "timestamp": 1638945588.7289119
}
```
