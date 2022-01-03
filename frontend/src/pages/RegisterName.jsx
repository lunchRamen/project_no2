import React, { useState } from "react";
import axios from "axios";
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

function Register() {
  const dispatch = useDispatch();
  const [inputs, setInput] = useState({
    userId: "",
    userPw: "",
    userNickname: "",
    userBirth: "",
    userGender: "",
    userJob: "",
    userLive: "",
    userTime: "",
    usableId: false,
  });

  const { userId, userPw, userNickName, usableId } = inputs;

  const [overIdLength, setOverIdLength] = useState(false);
  const [overPwLength, setOverPwLength] = useState(false);

  const onChange = (e) => {
    const { value, name } = e.target;
    setInput({
      ...inputs,
      [name]: value,
      usableId: usableId,
    });
    console.log(name);
    if (inputs.userId.length > 8) {
      setOverIdLength(true);
    } else {
      setOverIdLength(false);
    }
    if (inputs.userPw.length > 12) {
      setOverPwLength(true);
    } else {
      setOverPwLength(false);
    }
  };
  const checkId = (e) => {
    e.preventDefault();
    if (overIdLength) {
      return;
    }
    axios
      .post(`/regiser/checkId/${userId}`, { id: userId })
      .then((response) => {
        if (response.status === 200) {
          setInput({
            ...inputs,
            usableId: true,
          });
          alert("사용가능한 아이디입니다.");
        }
      })
      .catch((error) => {
        console.log(error);
        alert("이미 사용중인 아이디입니다.");
      });
  };

  const SignUp = (e) => {
    const navigate = useNavigate();
    e.preventDefault();
    let body = {
      id: userId,
      password: userPw,
      nickname: userNickName,
    };
    if (overIdLength || overPwLength) {
      return;
    } else if (!userId || !userPw || !userNickName) {
      alert("필수 항목을 작성해주세요");
      return;
    } else if (usableId === false) {
      alert("아이디 중복 확인을 해주세요");
      return;
    } else {
      dispatch(registerUser(body))
        .then((response) => {
          if (response.payload.success) {
            alert("다음 항목으로 이동하겠습니다.");
            navigate("./register/detail");
          } else {
            alert("회원가입에 실패했습니다.");
          }
        })
        .catch((error) => console.log(error));
    }
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
                  name="userId"
                  type="text"
                  placeholder="아이디"
                  onChange={onChange}
                  value={userId}
                />
                {overIdLength && <LimitOnLength>아이디를 8자 이내로 입력해주세요</LimitOnLength>}
                <CheckIdButton onClick={checkId}>중복체크</CheckIdButton>
              </form>
              <form onSubmit={SignUp}>
                <RegisterInput
                  labelName="비밀번호"
                  name="userPw"
                  type="password"
                  placeholder="비밀번호"
                  onChange={onChange}
                  value={userPw}
                />
                {overPwLength && <LimitOnLength>비밀번호를 12자 이내로 입력해주세요</LimitOnLength>}
                <RegisterInput
                  labelName="닉네임"
                  name="userNickname"
                  type="text"
                  placeholder="닉네임"
                  onChange={onChange}
                  value={userNickName}
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
