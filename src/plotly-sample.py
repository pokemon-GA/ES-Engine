# グラフ可視化
import plotly.graph_objects as go


fig = go.Figure()

gen_number = list(range(1,101,1))

fig.add_trace(
    go.Scatter(x = gen_number, #X_label
               y = gen_number, #y_label
              text = "1st", #
              mode = 'lines', #折れ線グラフ
              name = 'default(solid)', #line_type
              line=dict(color='firebrick', width=4) #line_type_detail      
    )
)
fig.add_trace(
    go.Scatter(x = gen_number,
               y = gen_number,
              text = "2nd",
              mode = 'lines',
              name = 'solid + 太め',
              line=dict(color='firebrick', width=10,dash='solid')  
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = gen_number,
              text = "3rd",
              mode = 'lines',
              line=dict(color='firebrick', width=4,dash='dot'),
              name = 'dot'
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = gen_number,
              text = "4th",
              mode = 'lines',
              line=dict(color='firebrick', width=4,dash='dash'),
              name = 'dash'
    )
)

fig.update_layout(
    xaxis_title = 'Generation',
    yaxis_title = 'Totla Score'
)

    
fig.show()