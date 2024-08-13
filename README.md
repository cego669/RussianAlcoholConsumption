# ❓ Problem: where should a drinks company run promotions?

The company owns a chain of stores across Russia that **sell a variety of alcoholic drinks**. The company recently ran a **wine promotion** in **Saint Petersburg** that was **very successful**. Due to the cost to the business, it isn’t possible to run the promotion in all regions. The marketing team would like **to target 10 other regions that have similar buying habits to Saint Petersburg** where they would expect the promotion to be similarly successful.

## 📈 The data

The marketing team has sourced with **historical sales volumes per capita for several different drinks types**.

- "year" - year (1998-2016)
- "region" - name of a federal subject of Russia. It could be oblast, republic, krai, autonomous okrug, federal city and a single autonomous oblast
- "wine" - sale of wine in litres by year per capita
- "beer" - sale of beer in litres by year per capita
- "vodka" - sale of vodka in litres by year per capita
- "champagne" - sale of champagne in litres by year per capita
- "brandy" - sale of brandy in litres by year per capita

## ✅ Solution proposed by this notebook

This notebook includes an [**interactive data exploration**](https://cego669.github.io/RussianAlcoholConsumption/) where you can **easily compare alcohol consumption patterns between different regions of Russia**. As a solution to the business problem, the [Dynamic Time Warping (DTW)](https://en.wikipedia.org/wiki/Dynamic_time_warping) technique was used to calculate the distance between time series of the same drink from different regions. In this way, using [Principal Component Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis), **it was possible to project the distances between all regions on a plane**, where **it is easy to visualize the regions most similar to Saint Petersburg in terms of alcohol consumption pattern**.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Carlos Eduardo Gonçalves de Oliveira - [linkedin](https://www.linkedin.com/in/cego669/) - carlosedgonc@gmail.com

Project Link: [https://github.com/cego669/DirtyCategoriesEncoding](https://github.com/cego669/RussianAlcoholConsumption)
