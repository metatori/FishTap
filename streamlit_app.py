
import streamlit as st
import openai

st.set_page_config(page_title="멘싱스 GPT 뉴스 생성기", layout="centered")
st.title("멘싱스 - GPT 뉴스 생성 + 가격 감지")

# 예시 상품 정보
product = {
    "name": "LED 무드등 스탠드",
    "before": 29900,
    "after": 24900,
    "link": "https://link.coupang.com/a/sample"
}
price_drop = product['before'] - product['after']

# 프롬프트
prompt = f"""
'{product['name']}' 상품이 어제 {product['before']}원에서 오늘 {product['after']}원으로 {price_drop}원 인하되었습니다.
이 정보를 바탕으로 3문장짜리 뉴스 스타일 요약을 작성해주세요.
첫 문장은 가격 인하, 두 번째는 제품 특징, 세 번째는 소비자 반응을 상상해서 써주세요.
"""

# 상품 정보 출력
st.markdown(f"**상품명:** {product['name']}")
st.markdown(f"**가격 변화:** {product['before']}원 → {product['after']}원 (↓{price_drop}원)")
st.markdown(f"[▶️ 상품 보러가기]({product['link']})")
st.markdown("---")

# GPT 기사 생성
if st.button("🧠 GPT 뉴스 생성"):
    try:
        openai.api_key = st.secrets["openai_key"]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        article = response.choices[0].message.content
        st.success("뉴스 기사 생성 완료!")
        st.markdown("#### 결과:")
        st.write(article)
    except Exception as e:
        st.error(f"오류 발생: {e}")
