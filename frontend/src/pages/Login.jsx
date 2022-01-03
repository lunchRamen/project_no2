import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { loginUser } from "../_actions/user_actions";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import LoginInput from "../components/Login/LoginInput";
import LoginButton from "../components/Login/LoginButton";
import StyledContainer from "../components/Style/styledContainer";
import { theme } from "styled-tools";

function Login() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [inputs, setInputs] = useState({
    userId: "",
    userPw: "",
  });
  const { userId, userPw } = inputs;

  const onChange = (e) => {
    const { value, name } = e.target;
    setInputs({
      ...inputs,
      [name]: value,
    });
    //name에는 userId, userPw value에는 사용자가 입력한 값
  };
  const onSubmit = (e) => {
    e.preventDefault();
    let body = {
      id: userId,
      password: userPw,
    };
    if (!userId || !userPw) {
      alert("필수 항목을 작성하세요");
    } else {
      dispatch(loginUser(body)).then((data) => {
        if (data.payload.loginSuccess) {
          window.localStorage.setItem("userId", data.payload.userId);
          navigate("/main");
        }
        if (!data.payload.loginSuccess) {
          alert(data.payload.message);
        }
      });
    }
  };

  return (
    <StyledContainer>
      <div>
        <form onSubmit={onSubmit} style={{ textAlign: "center" }}>
          <LoginInput
            type="text"
            name="userId"
            placeholder="아이디를 입력해주세요"
            onChange={onChange}
            value={userId}
          />
          <LoginInput
            type="password"
            name="userPw"
            placeholder="비밀번호를 입력해주세요"
            onChange={onChange}
            value={userPw}
          />
          <LoginButton type="submit" isMini={true}>
            로그인
          </LoginButton>
        </form>
        <StyledDiv>
          <Link to="/register/name">
            <StyledSpan>식스맨 극장에 처음이신가요?</StyledSpan>회원가입
          </Link>
        </StyledDiv>
      </div>
    </StyledContainer>
  );
}
const StyledDiv = styled.div`
  text-align: center;
  margin-top: 2rem;
  font-weight: 500;
  font-size: 1.6rem;
  ${theme("neons.textNeonGold")};
`;
const StyledSpan = styled.span`
  color: white;
  font-weight: 300;
  margin-right: 1rem;
  letter-spacing: -0.05rem;
`;

export default Login;
