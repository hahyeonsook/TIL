## [Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/problem)

```oracle
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '[aeiouAEIOU]$')
    AND REGEXP_LIKE(CITY, '^[aeiouAEIOU]');
```

```oracle
SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '^[aeiouAEIOU].*[aeiouAEIOU]$');
```