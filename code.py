import web

render=web.template.render('templates/')
db=web.database(dbn='sqlite',db='MovieSite.db')

urls=(
	'/','index'
)

movies=[
    {
        'title':'Forrest Gump',
        'year':'1994',
    },
    {
        'title':'Titanic',
        'year':'1997',
    },
]

class index:
    def GET(self):
        
        movies=db.select('movie')
        return render.index(movies)



if __name__ == '__main__':
	app=web.application(urls,globals())
	app.run()

	

