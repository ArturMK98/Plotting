import plotly.express as px
from random_walk import RandomWalk

# Keep making random walks as long as program is active
while True:
    # Make a random walk
    steps = 50_000
    rw = RandomWalk(steps)
    rw.fill_walk()

    point_numbers = range(rw.num_points)
    title = f"Random Walk With {steps} Steps"
    fig = px.scatter(x=rw.x_values, y=rw.y_values, title=title, 
                     color=point_numbers, color_continuous_scale='Emrld')

    fig.update_layout(
        title=f"Random Walk With {steps} Steps",
        xaxis=dict(scaleanchor='y', showticklabels=False, title=''),
        yaxis=dict(scaleanchor='x', showticklabels=False, title=''),
    )

    fig.show()

    if input("Make another walk? (y/n): ") == 'n':
        break