/* eslint-disable prettier/prettier */
import React from 'react';
import styled from "styled-components";
import { theme } from "styled-tools";
import { Chart } from "../components";
import * as images from "../assets/images";

export default function Contents() {
  // const [age, setAge] = useState("");


  //  const fetchAgeGraph = async () => {
  //     const res = await client.post("user/register", { ...inputs, prefer_ott_content_genres: selectedList });
  //     console.log(`res`, res);
  //     navigate("/register/done");
  // };

  // const CheckAge = (age) => {
  //   if(age==="10s") setAge("10대사진 링크");
  //   if(age==="20s") setAge("20대사진 링크");
  //   if(age==="30s") setAge("30대사진 링크");
  //   if(age==="40s") setAge("40대사진 링크");
  //   if(age==="50s") setAge("50대사진 링크"); 
  // }
  return (
      <Wrap>
        <LandingPage>하늘 님은 20대 남성 회사원이시고,  19시~23시 서울에서 비대면 극장에 접속하십니다.<br/>
          주로 스릴러, 액션, 로맨스 콘텐츠를 좋아하시는군요!</LandingPage>
        <LandingPage>사용자님과 같은 나이대 분들이 시청하는 시간대입니다.</LandingPage>
        <WrapImg>
          <Image src={images.age10_2019} alt="age image" />
          <Image src={images.age10_2020} alt="age image" /><br/>
        </WrapImg>

        <LandingPage>넷플릭스에서 서비스 중인 장르들</LandingPage>
        <WrapWord>
        <Image src={images.word} alt="word image" />
        </WrapWord>

        <LandingPage>한국 넷플릭스의 장르변화 2019-2020</LandingPage>
        <WrapNetflix>
        <Image src={images.netflix} alt="netflix image" />
        </WrapNetflix>
        
      <ChartWrap>
        <Chart></Chart>
        <Chart></Chart>
        <Chart></Chart>
      </ChartWrap>
      </Wrap>
  );
}
// background-image: url(${footer});
const Wrap = styled.main`
  // display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 100vw;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 38rem;
    height: 19rem;
  }
`;

const ChartWrap = styled.div`
  // display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  
  width: 50vw;
  height: 40vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 38rem;
    height: 19rem;
  }
`;

const LandingPage = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  margin-top: 5rem;
`;
const Image = styled.img`
  margin: 3rem 0;
  border: 0.1rem solid ${theme("colors.mainBlack")};
  border-radius: 2rem;
`;
const WrapImg = styled.div`
  display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 10rem auto;
  
  width: 50vw;
  height: 40vh;

  & > img {
    width: 90rem;
    height: 60rem;
  }
`;

const WrapWord = styled.div`
  display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 1rem auto;
  
  width: 50vw;
  height: 40vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 70rem;
    height: 50rem;
  }
`;

const WrapNetflix = styled.div`
  display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 10rem auto;
  
  width: 50vw;
  height: 40vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 130rem;
    height: 60rem;
  }
`;
// const ButtonWrapper = styled.div`
//   display: flex;
//   justify-content: space-between;
//   margin-bottom: 10rem;
//   width: 87rem;
//   ${theme("fonts.textH2")}
//   ${theme("neons.textNeonGold")};
// `;

// const LandingButton = styled.span`
//   cursor: pointer;
//   border-bottom: 0.1rem solid ${theme("colors.mainBlack")};
//   padding: 2rem 3.5rem;
//   color: ${theme("colors.mainWhite")};
//   ${theme("neons.textNeonGold")}

//   &:hover {
//     color: ${theme("colors.mainPoint")};
//     border-color: ${theme("colors.mainPoint")};
//   }
// `;
