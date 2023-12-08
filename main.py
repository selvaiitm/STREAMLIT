import streamlit as st


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<h1 align="center">  STREAMLIT APP </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> THIS IS AN VERY BASIC LEVEL APP CREATED AS PART OF WEEKLY ASSIGNMENT FOR THE BS IN DATA SCIENCE COURSE OFFERED BY IIT MADRAS FOR THE SUBJECT NAMED TOOLS IN DATA SCIENCE 
""", unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> WEEK - 8 GRADED ASSIGNMENT </h3>
""", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> AN APP TO FIND THE LARGEST OF THE THREE GIVEN NUMBERS </h3>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


def largest(a,b,c):
    if a>=b:
        if a>=c:
            return a
        return c
    else:
        if b>=c:
            return b
        return c

a = st.number_input('Enter the first digit:')
b = st.number_input('Enter the second digit:')
c = st.number_input('Enter the third digit:')

larger = largest(a,b,c)

st.markdown("<hr>", unsafe_allow_html=True)

text = f' Among the given numbers {a} , {b} and {c}'

st.markdown(f"""
<h3 align="center">{text}
""", unsafe_allow_html=True)
# st.write(f' Among the given numbers {a} , {b} and {c}')

data = []
data.append(a)
data.append(b)
data.append(c)


st.bar_chart(data)

st.markdown("<hr>", unsafe_allow_html=True)

text2 = f'{larger} is the largest number'

st.markdown(f"""
<h3 align="center">{text2}
""", unsafe_allow_html=True)


# st.write(f" {larger} is the largest number")

large = []
large.append(larger)

st.bar_chart(large)





