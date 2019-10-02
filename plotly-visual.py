#%%
# import required libraries
import plotly.express as px


#%%
gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
fig.show()

#%%
import chart_studio
import chart_studio.plotly as py

#%%
username='deolgurpreet'
api_key='SlRW3lS2KG9slmE0XOMm'
chart_studio.tools.get_credentials_file(username,api_key)

#%%
py.plot(fig,filename='gdp_per_cap', auto_open=True)
