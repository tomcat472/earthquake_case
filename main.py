import pandas as pd
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
logo=Image.open("logo/ccsc_sfc_logo.png")
st.set_page_config(
    layout="wide",
    page_icon=logo,
    page_title="CDM case (Earthquake)",
    initial_sidebar_state="expanded"
)
col1,col2 = st.columns([1,4])
with col1:
    st.image("logo\ccsc_sfc_logo.png",width=300)
with col2:
    st.markdown("")
    st.markdown("")
    st.markdown("# စစ်ကိုင်းဖက်ဒရယ်ယူနစ် CDM နိုင်ငံဝန်ထမ်းများကောင်စီ")
    st.markdown("")
st.write("")
df=pd.read_csv("ccsc_sfu.csv")
# st.dataframe(df.sample(5))
with st.expander("## စစ်ကိုင်းမြေငလျင်ဒဏ်ခံ CDM များကို ထောက်ပံ့ခြင်း"):
    st.write("""
                + CDM နိုင်ငံ့ဝန်ထမ်းများ ကောင်စီ- စစ်ကိုင်းဖက်ဒရယ်ယူနစ်  (CCSC-SFU) စတင်ဖွဲ့စည်းသည်မှ စ၍ စစ်ကိုင်းတိုင်းအတွင်း CDM များကို တက်နိုင်သလောက် ချိတ်ဆက်၍ CDM များ၏ အကျိုးစီးပွားကို ဆောင်ရွက်ပေးလျှက်ရှိပါသည်။
            """)
    st.write("""
                + မတ်လ ၂၈ ရက်နေ့တွင် လှုပ်ခက်သွားသော စစ်ကိုင်းမြေငလျင်သည် ပြည်သူများ၏ အသက်အိုးအိမ် စည်းစိမ်များကို အောက်ခြေမှ ကိုင်လှုပ်လိုက်သလို  ဖျက်စီးရာတွင် တိုင်းပြည်အတွက် အနစ်နာခံ CDM ဆောင်ရွက်လျှက်ရှိသည့် CDM  နိုင်ငံဝန်ထမ်းများပါ ထိခိုက်ပျက်စီးသည့်အထဲ ပါဝင်ခဲ့ပါသည်။ 
        """)
    st.write("""
                + CCSC-SFU သည် မြေငလျင်ဒဏ် ထိခိုက်သူများထဲမှ အသက်အိုးအိမ် ထိခိုက်နစ်နာသူ CDM များစာရင်းကို ကောက်ယူခဲ့ပါသည်။ နေအိမ်လုံးဝပျက်စီးသည့် CDM များနှင့် တစိတ်တပိုင်းပျက်ဆီးစာရင်းများအပြင် ၊ မိသားစုတွင်း အသက်သေဆုံသူများနှင့် ထိခိုက်ဒဏ်ရာကသူများလည်း တွေ့ရှိရပါသည်။
            """)
    st.write("""
                + CDM များအနေဖြင့် အမျိုးသား၊ အမျိုးသမီး အရေအတွက် မကွာတာကို တွေ့ရှိရပါသည်။
            """)
    st.write("""
                + ဝန်ကြီးဌာနအလိုက်အနေဖြင့် ပို့ဆောင်ရေးနှင့် ဆက်သွယ်ရေးဝန်ကြီးဌာနရှိ မီးရထားဌာနကို အများဆုံးထောက်ပံ့ နိုင်ခဲ့ပြီး၊ ပညာရေးဌာနမှ CDM ဝန်ထမ်းများကိုလည်း ထောက်ပံ့ပေးနိုင်ခဲ့ပါသည်။
            """)
    st.write("""
                + မြို့နယ်အလိုက်တွင်လည်း မြေငလျင်ဒဏ်ကို အဓိကခံစားခဲ့ရသည့် စစ်ကိုင်းမြို့နယ်ကို အများဆုံးထောက်ပံ့ခဲ့ပြီး စစ်ကိုင်းဖက်ဒရယ်ယူနစ် ပြင်ပ CDM များကိုလည်း အနည်းငယ်ထောက်ပံ့ပေးနိုင်ခဲ့ပါသည်။
            """)

st.markdown("""
<style>
    /* --- Make Tab Text Larger --- */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 30px; /* Adjust font size as needed */
    }

    /* --- Add Space Between Tabs --- */
    .stTabs [data-baseweb="tab-list"] button {
        margin-right: 10px; /* Adjust this value for more or less space */
        /* You could also use margin-left if you prefer */
    }

    /* Optional: Remove margin from the last tab button if it looks off */
    /*
    .stTabs [data-baseweb="tab-list"] button:last-child {
        margin-right: 0px;
    }
    */
</style>
""", unsafe_allow_html=True)



tab1, tab2, tab3 = st.tabs(["Ministry", "District", "Township"])

with tab1:
    ministry=df.ministries.value_counts().index
    selected_ministry=st.selectbox("Choose Ministry",ministry)
    # st.header(f"{selected_ministry}")
    filter_df=df[df.ministries==selected_ministry].cdm_townships.value_counts()
    col3,col4=st.columns([1,1])
    with col3:
        fig = px.bar(filter_df, x=filter_df.index, y=filter_df.values,title=f"CDM ပြုလုပ်ခဲ့သော မြို့နယ်အလိုက် မြေငလျင်ဒဏ်ခံ CDM စာရင်း",text_auto='.1s')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False,marker_color="#2500F4")
        fig.update_xaxes(tickangle=-90)
        fig.update_layout(width=800,height=500)
        fig.update_layout(xaxis_title=None, yaxis_title=None)
        col3.plotly_chart(fig)
    with col4:
        filter_df=df[df.ministries==selected_ministry].current_living_district.value_counts()
        fig = px.bar(filter_df, x=filter_df.index, y=filter_df.values,
                title=f"လက်ရှိနေထိုင်သောခရိုင်အလိုက် မြေငလျင်ဒဏ်ခံ CDM စာရင်း",text_auto='.1s')
        fig.update_traces(
            marker_color='#F90707', 
            textfont_size=12,
            textangle=0,
            textposition="outside",
            cliponaxis=False
        )
        fig.update_xaxes(tickangle=-90)
        fig.update_layout(xaxis_title=None, yaxis_title=None) 
        col4.plotly_chart(fig)
    
    
    filter_df=df[df.ministries==selected_ministry]
    selected_columns=filter_df[["pregnant","five_years_old_children","PWD","house_destroyed","house_damaged","cdm_injured","cdm_family_member_deaths","cdm_family_member_injured"]].columns
    columns_selected=st.selectbox(label="Cases",options=selected_columns)
    
    counts=filter_df[columns_selected].value_counts()
    st.dataframe(counts,use_container_width=True)
         
    custom_colors = ["#0222F5", "#DD8FCC"] 
    
    col5,col6,col7=st.columns([1,1,1]) 
    pie_plot=px.pie(counts,
                        title=f"{columns_selected.title()} Distribution",
                                values=counts.values,
                                names=counts.index,
                                color_discrete_sequence=custom_colors)
    pie_plot.update_traces(textinfo='value')
    col6.plotly_chart(pie_plot)    
    
with tab2:
    districts=df.current_living_district.value_counts().index
    selected_districts=st.selectbox("Choose District",districts)
    st.header(f"{selected_districts}")
    
    col8,col9=st.columns([1,1])
    with col8:
        filter_df=df[df.current_living_district==selected_districts].cdm_townships.value_counts()
        fig = px.bar(filter_df, x=filter_df.index, y=filter_df.values,title=f"CDM ပြုလုပ်ခဲ့သော မြို့နယ်အလိုက် မြေငလျင်ဒဏ်ခံ CDM စာရင်း",text_auto='.1s')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False,marker_color="#2500F4")
        fig.update_xaxes(tickangle=-90)
        fig.update_layout(width=800,height=500)
        fig.update_layout(xaxis_title=None, yaxis_title=None)
        col8.plotly_chart(fig)
    
    with col9:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        filter_df=df[df.current_living_district==selected_districts].ministries.value_counts()
        col9.dataframe(filter_df)
    
    
    filter_df=df[df.current_living_district==selected_districts]
    selected_columns=filter_df[["pregnant","five_years_old_children","PWD","house_destroyed","house_damaged","cdm_injured","cdm_family_member_deaths","cdm_family_member_injured"]].columns
    columns_selected=st.selectbox(label="Cases",options=selected_columns,key="districts")
    
    counts=filter_df[columns_selected].value_counts()
    st.dataframe(counts,width=1000)
         
    custom_colors = ["#0222F5", "#DD8FCC"] 
    
    col10,col11,col12=st.columns([1,1,1]) 
    pie_plot=px.pie(counts,
                        title=f"{columns_selected.title()} Distribution",
                                values=counts.values,
                                names=counts.index,
                                color_discrete_sequence=custom_colors)
    pie_plot.update_traces(textinfo='value')
    col11.plotly_chart(pie_plot)

with tab3:
    township=df.cdm_townships.value_counts().index
    selected_cdm_townships=st.selectbox("Choose Township",township)
    st.header(f"{selected_cdm_townships}")
    
    col12,col13=st.columns([1,1])
    with col12:
        filter_df=df[df.cdm_townships==selected_cdm_townships].current_living_district.value_counts()
        fig = px.bar(filter_df, x=filter_df.index, y=filter_df.values,title=f"မြေငလျင်ဒဏ်ခံ CDM များ၏ ခရိုင်အလိုက် နေထိုင်မှုစာရင်း",text_auto='.1s')
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False,marker_color="#2500F4")
        fig.update_xaxes(tickangle=-90)
        fig.update_layout(width=800,height=500)
        fig.update_layout(xaxis_title=None, yaxis_title=None)
        col12.plotly_chart(fig)
    
    with col13:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        filter_df=df[df.cdm_townships==selected_cdm_townships].ministries.value_counts()
        col13.dataframe(filter_df)
    
    
    filter_df=df[df.cdm_townships==selected_cdm_townships]
    selected_columns=filter_df[["pregnant","five_years_old_children","PWD","house_destroyed","house_damaged","cdm_injured","cdm_family_member_deaths","cdm_family_member_injured"]].columns
    columns_selected=st.selectbox(label="Cases",options=selected_columns,key="townships")
    
    counts=filter_df[columns_selected].value_counts()
    st.dataframe(counts,width=1000)
         
    custom_colors = ["#0222F5", "#DD8FCC"] 
    
    col14,col15,col16=st.columns([1,1,1]) 
    pie_plot=px.pie(counts,
                        title=f"{columns_selected.title()} Distribution",
                                values=counts.values,
                                names=counts.index,
                                color_discrete_sequence=custom_colors)
    pie_plot.update_traces(textinfo='value')
    col15.plotly_chart(pie_plot)