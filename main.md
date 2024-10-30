**13th Page:**

To summarize, our team’s primary goal is to mitigate disaster risks and related challenges. Specifically, our solution addresses the difficulty of managing expiration dates, the challenges of stockpiling, and the reduction of food waste from stockpiled supplies.

**Solution:** We utilize Rakuten Ichiba and Rakuten Recipe to recommend purchases for soon-to-expire items and suggest recipes using items that are nearing expiration.

**14th Page:**

The server offers three endpoints that can be accessed for retrieving or modifying data. The `/stocks/` and `/users/` endpoints handle various data operations related to users and items in the database. The `Recipes API` simulates the Rakuten Recipes API. Additionally, the frontend will integrate APIs provided by Rakuten.

**15th Page:**

Our application features three main capabilities: stock management, suggestion generation, and recipe search.

- **Stock Management:** Displays details of all items the user possesses and allows for data modifications.
- **Suggestion Generation:** Offers recommendations for purchases and recipes based on data from Rakuten Recipes and Rakuten Michiba.
- **Recipe Search:** Assists users in finding suitable recipes based on their search criteria.

**23rd Page:**

For the backend, we use Google Cloud’s free server to host our application. The backend is developed in Python, with FastAPI—a rapidly emerging framework—as the server framework. We manage the database using SQLite in combination with SQLAlchemy, a robust Object-Relational Mapping (ORM) framework that streamlines database operations.

**25th Page:**

Looking ahead, we envision enhancing the application with three additional features:

1. **Enhanced Recommendations:** Offer more personalized suggestions based on the buyer’s preferences.
2. **Integration with Additional Platforms:** Broaden the range of sources for suggestions and recipes.
3. **Expiration Alerts:** Introduce a notification system to alert users when items are approaching their expiration dates.