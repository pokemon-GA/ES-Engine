import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

# go.Scatterはデフォルトで折れ線グラフ

np.random.seed(1)
x = np.arange(10)

print(x)

plot = [go.Scatter(x=x, y=np.random.randn(10))]
fig = go.Figure(data=plot)

# グラフ全体とホバーのフォントサイズ変更
fig.update_layout(font_size=20, hoverlabel_font_size=20)
fig.show()