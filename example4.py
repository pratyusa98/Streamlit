## Displaying JSON
import streamlit as st

st.text("Display JSON")
st.json({'name':"Jesse",'gender':"male"})

## Displaying Raw Code and JSON
## In case you want to display the raw preformatted code you can use the st.code() or st.echo()

# Displaying Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")


# Display Raw Code 
with st.echo():
	# This will also show as a comment
	import numpy as np
	import pandas as pd 
	df = pd.DataFrame()