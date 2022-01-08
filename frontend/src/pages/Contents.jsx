/* eslint-disable prettier/prettier */
import styled from "styled-components";
import { theme } from "styled-tools";
import { Chart } from "../components";
import * as images from "../assets/images";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Contents() {
  const [userData1, setUserData1] = useState([]);
  const [userData3, setUserData3] = useState([]);
  const [userData5, setUserData5] = useState([]);
  const [age, setAge] = useState("");

  const fetchData1 = async (token) => {
    axios.defaults.headers.common["Authorization"] = `JWT ${token}`;
    axios.post("http://127.0.0.1:8000/api/contents-analysis/1").then((res) => setUserData1(res.data.data));
  };

  const fetchData3 = async (token) => {
    axios.defaults.headers.common["Authorization"] = `JWT ${token}`;
    axios
      .post("http://127.0.0.1:8000/api/contents-analysis/3", {
        headers: {
          Authorization: `JWT ${token}`,
        },
      })
      .then((res) => setUserData3(res.data));
  };

  const fetchData5 = async (token) => {
    axios.defaults.headers.common["Authorization"] = `JWT ${token}`;
    axios
      .post("http://127.0.0.1:8000/api/contents-analysis/5", {
        headers: {
          Authorization: `JWT ${token}`,
        },
      })
      .then((res) => setUserData5(res.data));
  };

  useEffect(() => {
    const userToken = window.localStorage.getItem("token");
    fetchData1(userToken);
    fetchData3(userToken);
    fetchData5(userToken);
  }, []);

  useEffect(() => {
    setAge(userData1?.age?.split("_")[1].split("s")[0]);
  }, [userData1]);

  useEffect(() => {
    console.log(`userData3`, userData3);
  }, [userData3]);

  return (
    <Wrap>
      {age && userData1 && (
        <LandingPage>
          {userData1.username}님은 {age}대 {userData1.gender}이시고, {userData1.watch_time}대에 주로 콘텐츠를
          시청하시는군요!
          <br />
          주로 {userData1.user_genres?.join(", ")} 콘텐츠를 좋아하시는군요!
        </LandingPage>
      )}

      <LandingPage>사용자님과 같은 나이대 분들이 시청하는 시간대입니다.</LandingPage>
      <WrapImg>
        <Image src={images[`age${age}_2019`]} alt="age image" />
        <Image src={images[`age${age}_2020`]} alt="age image" />
        <br />
      </WrapImg>
      <LandingPage>넷플릭스에서 서비스 중인 장르들</LandingPage>
      <WrapWord>
        <Image src={images.word} alt="word image" />
      </WrapWord>

      <LandingPage>한국 넷플릭스의 장르변화 2019-2020</LandingPage>
      <WrapNetflix>
        <Image src={images.netflix} alt="netflix image" />
      </WrapNetflix>

      {userData1 && userData3 && userData5 && (
        <ChartWrap>
          {userData3.map((chartData, idx) => {
            const mention = chartData.people.split("_")[1];
            const isGender = mention.includes("male") ? true : false;
            return (
              <>
                <LandingPage>
                  {userData1.username}과 같은 {isGender ? "성별" : "나이대"}의 사람들
                </LandingPage>
                <Chart key={idx} data={chartData.data} genreName={chartData.review_genre} />
              </>
            );
          })}
        </ChartWrap>
      )}

      {userData1 && userData5 && (
        <ChartWrap>
          {userData5.map((chartData, idx) => (
            <>
              <LandingPage>
                {userData1.username}님이 좋아하는 {chartData.review_genre}를 좋아하는 사람들
              </LandingPage>
              <Chart key={idx} data={chartData.data} genreName={chartData.review_genre} />
            </>
          ))}
        </ChartWrap>
      )}
    </Wrap>
  );
}
// background-image: url(${footer});
const Wrap = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10rem;
  padding-top: 15rem;

  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 38rem;
    height: 19rem;
  }
`;

const ChartWrap = styled.div`
  display: flex;
  flex-direction: column;
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

export const LandingPage = styled.div`
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
