SELECT country, date,
	CASE
	WHEN daily_vaccinations IS NULL
	THEN ISNULL(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) OVER (PARTITION BY country),0)
	ELSE daily_vaccinations
	END AS daily_vaccinations,
	vaccines
FROM [dbo].[country_vaccination_stats]