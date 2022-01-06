import React, { useState, useEffect } from "react";
import { Button, SelectList } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { useNavigate, useLocation } from "react-router-dom";
import Fade from "react-reveal/Fade";
// import { useDispatch } from "react-redux";
// import { registerUser } from "../_actions/user_actions";
const TEMP_SELECTION_DATA = [
  {
    id: "job",
    label: "님이 어떤 일을 하시는 분인지 궁금해요!",
    option_list: [
      { id: 0, value: "학생" },
      { id: 1, value: "서비스/판매직" },
      { id: 2, value: "주부" },
      { id: 3, value: "사무직" },
      { id: 4, value: "무직" },
      { id: 5, value: "생산직" },
      { id: 6, value: "기타" },
    ],
  },
  {
    id: "region",
    label: "어디에 거주하시나요?",
    option_list: [
      { id: 0, value: "주거 1" },
      { id: 1, value: "주거 2" },
      { id: 2, value: "주거 3" },
      { id: 3, value: "주거 3" },
      { id: 4, value: "주거 4" },
    ],
  },
  {
    id: "watch_time",
    label: "주로 어떤 시간대에 영상을 시청하시나요??",
    option_list: [
      { id: 0, value: "시간대 1" },
      { id: 1, value: "시간대 2" },
      { id: 2, value: "시간대 3" },
      { id: 3, value: "시간대 3" },
      { id: 4, value: "시간대 4" },
    ],
  },
];

export default function RegisterStep() {
  const navigate = useNavigate();
  const location = useLocation();
  // const dispatch = useDispatch();
  const [inputs, setInputs] = useState("");

  const { birth_day, gender, job, region, watch_time } = inputs;
  //user_id, password1, nickname,
  // console.log(inputs);
  useEffect(() => {
    setInputs(location.state.inputs);
  }, []);

  const SignUp = (e) => {
    e.preventDefault();
    // const body = {
    //   id: user_id,
    //   password: password1,
    //   nickname: nickname,
    //   birth_day: birth_day,
    //   gender: gender,
    //   job: job,
    //   region: region,
    //   watch_time: watch_time,
    // };
    if (!birth_day || !gender || !job || !region || !watch_time) {
      alert("작성되지 않은 항목이 있습니다.");
      return;
    }
    alert("다음 항목으로 이동하겠습니다.");
    navigate("/register/step3", { state: { inputs: inputs } });
    // dispatch(registerUser(body))
    //   .then(({ data }) => {
    //     const isSuccess = data.payload.success;
    //     if (isSuccess) {
    //       // console.log(body);
    //       alert("다음 항목으로 이동하겠습니다.");
    //       navigate("./register/step3");
    //     }
    //     if (!isSuccess) {
    //       alert("회원가입에 실패했습니다.");
    //     }
    //   })
    //   .catch((error) => console.log(error));
  };
  return (
    <Wrapper>
      <Fade>
        <Intro>
          님에게 꼭 맞는 비대면 극장을 추천해드릴게요!
          <br />
          기본적인 정보만을 수집하고, 분석 이외의 목적으로는 절대 사용되지 않습니다.
        </Intro>
        <SelectList data={TEMP_SELECTION_DATA} inputs={inputs} setInputs={setInputs} />
        <Button isMini={false} onClick={SignUp}>
          다음으로(2/3)
        </Button>
      </Fade>
    </Wrapper>
  );
}

const Wrapper = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10rem;
  padding-top: 12rem;
  padding-bottom: 50rem;
`;

const Intro = styled.span`
  text-align: center;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")}
`;
