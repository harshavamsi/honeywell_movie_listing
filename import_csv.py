import csv

from movielisting.models import Movie
def main():

    csv_file       = "movie_data.csv"
    count          = 0


    #Delete all existing teams and participants from the database.
    Movie.objects.all().delete()

    with open(csv_file) as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    for item in data:
        if item[0]:
            count += 1
            m = Movie.objects.create(
                movie_title=item[11].strip(),
                director_name =item[1].strip(),
                actor_1_name = item[10].strip(),
                actor_2_name = item[6].strip(),
                genres = item[9].strip(),
                language = item[19].strip(),
                country = item[20].strip(),
                content_rating = item[21].strip(),
                budget = item[22].strip(),
                title_year = item[23].strip(),
                plot_keywords = item[16].strip(),
                movie_imdb_link = item[17].strip()
            )

    print "{} movies imported.".format(count)

main()
