import React, { useState } from "react";
// import axios from "axios";
import styled from "styled-components";
import { theme } from "styled-tools";
import StyledBox from "../components/Style/styledBox";
import StyledContainer from "../components/Style/styledContainer";
import CheckIdButton from "../components/Register/CheckIdButton";
import RegisterInput from "../components/Register/RegisterInput";
import LimitOnLength from "../components/Register/LimitOnLength";
import RegisterButton from "../components/Register/RegisterButton";
import { useDispatch } from "react-redux";
import { registerUser } from "../_actions/user_actions";
import { useNavigate } from "react-router-dom";
import Fade from "react-reveal/Fade";

function Register({ location }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [inputs, setInput] = useState({
    user_id: "",
    password1: "",
    password2: "",
    nickname: "",
    birth_day: "",
    gender: "1",
    job: "",
    region: "",
    watch_time: "",
    usableId: true,
    prefer_ott_content_genre: [],
  });
  console.log(location);
  const { user_id, password1, password2, nickname, usableId } = inputs;

  const [checkIdLength, setOverIdLength] = useState(false);
  const [checkPwLength, setOverPwLength] = useState(false);
  const isOverLength = (inputValueLength, maxLength) => {
    if (inputValueLength > maxLength) {
      return true;
    }
  };

  const onChange = (e) => {
    const { value, name } = e.target;
    setInput({
      ...inputs,
      [name]: value,
      usableId: usableId,
    });
    const isUserIdOverLength = isOverLength(inputs.user_id.length, 8);
    if (isUserIdOverLength) {
      setOverIdLength(true);
    }
    if (!isUserIdOverLength) {
      setOverIdLength(false);
    }
    if (isOverLength(inputs.password1.length, 12)) {
      setOverPwLength(true);
      //패스워드와 아이디의 길이제한
    }
    if (!isOverLength(inputs.password1.length, 12)) {
      setOverPwLength(false);
    }
  };
  //아이디 중복확인하는 부분
  const checkId = (e) => {
    e.preventDefault();
    if (checkIdLength) {
      return;
    }
    // axios
    //   .post(`/regiser/checkId/${user_id}`, { id: user_id })
    //   .then((response) => {
    //     if (response.status === 200) {
    //       setInput({
    //         ...inputs,
    //         usableId: true,
    //       });
    //       alert("사용가능한 아이디입니다.");
    //     }
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //     alert("이미 사용중인 아이디입니다.");
    //   });
  };

  // const SignUp = (e) => {
  //   // const navigate = useNavigate();
  //   e.preventDefault();
  //   if (checkIdLength || checkPwLength) {
  //     return;
  //   } else if (!user_id || !password1 || !nickname) {
  //     alert("필수 항목을 작성해주세요");
  //     return;
  //   } else if (usableId === false) {
  //     alert("아이디 중복 확인을 해주세요");
  //     return;
  //   } else {
  //     navigate("/register/step2", { state: { inputs: inputs } });
  //   }
  // };

  const SignUp = (e) => {
    e.preventDefault();
    const body = {
      id: user_id,
      password: password1,
      nickname: nickname,
    };
    if (checkIdLength && checkPwLength) {
      return;
    }
    if (password1 !== password2) {
      alert("비밀번호를 다시 확인해주세요.");
      return;
    }
    if (!user_id || !password1 || !nickname) {
      alert("필수 항목을 작성해주세요");
      return;
    }
    if (usableId === false) {
      alert("아이디 중복 확인을 해주세요");
      return;
    }
    alert("다음 항목으로 이동하겠습니다.");
    navigate("/register/step2", { state: { inputs: inputs } });
    dispatch(registerUser(body))
      .then(({ data }) => {
        const isSuccess = data.payload.success;
        if (isSuccess) {
          console.log(body);
          alert("다음 항목으로 이동하겠습니다.");
          navigate("./register/step2");
        }
        if (!isSuccess) {
          alert("회원가입에 실패했습니다.");
        }
      })
      .catch((error) => console.log(error));
  };

  return (
    <>
      <Fade>
        <Wrap>
          <p>반갑습니다!</p>
          <p>비대면 극장 식스맨을 찾아주셔서 감사합니다.</p>
          <p>회원가입 진행을 위해 아이디와 비밀번호, 닉네임을 설정해주시기 바랍니다.</p>
        </Wrap>
        <StyledContainer>
          <div>
            <StyledBox padding="18px, 16px" lineHeight="20px">
              <form onSubmit={checkId}>
                <RegisterInput
                  labelName="아이디"
                  name="user_id"
                  type="text"
                  placeholder="아이디"
                  onChange={onChange}
                  value={user_id}
                />
                {checkIdLength && <LimitOnLength>아이디를 8자 이내로 입력해주세요</LimitOnLength>}
                <CheckIdButton onClick={checkId}>중복체크</CheckIdButton>
              </form>
              <form onSubmit={SignUp}>
                <RegisterInput
                  labelName="비밀번호"
                  name="password1"
                  type="password"
                  placeholder="비밀번호"
                  onChange={onChange}
                  value={password1}
                />
                {checkPwLength && <LimitOnLength>비밀번호를 12자 이내로 입력해주세요</LimitOnLength>}
                <RegisterInput
                  labelName="비밀번호 확인"
                  name="password2"
                  type="password"
                  placeholder="비밀번호 확인"
                  onChange={onChange}
                  value={password2}
                />
                <RegisterInput
                  labelName="닉네임"
                  name="nickname"
                  type="text"
                  placeholder="닉네임"
                  onChange={onChange}
                  value={nickname}
                />
                <RegisterButton type="submit">다음으로</RegisterButton>
              </form>
            </StyledBox>
          </div>
        </StyledContainer>
      </Fade>
    </>
  );
}
const Wrap = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 30vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};
`;
export default Register;
