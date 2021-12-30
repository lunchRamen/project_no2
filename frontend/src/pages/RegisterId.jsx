// import { Button } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { Link } from "react-router-dom";
export default function RegisterId() {
  return (
    <>
      <Wrap>
        <p>반갑습니다. 님!</p>
        <p>비대면 극장 식스맨을 찾아주셔서 감사합니다.</p>
        <p>회원가입 진행을 위해 아이디와 비밀번호를 설정해주시기 바랍니다.</p>
      </Wrap>

      <Wrap>
        <WrapIn>
          <IdWrap>
            <p>아이디</p>
            <Input
              type="text"
              name="name"
              style={{ color: "white", width: "33rem", fontSize: "2rem" }}
              placeholder="아이디를 입렫해주세요"></Input>
          </IdWrap>
          <LandingButton isMini={true}>중복확인</LandingButton>
        </WrapIn>
        <PassWrap>
          <p>비밀번호</p>
          <Input
            type="password"
            name="name"
            style={{ color: "white", width: "50rem", fontSize: "2rem" }}
            placeholder="비밀번호를 설정해주세요"></Input>
        </PassWrap>

        <PassconWrap>
          <p>비밀번호확인</p>
          <Input
            type="password"
            name="name"
            style={{ color: "white", width: "50rem", fontSize: "2rem" }}
            placeholder="비밀번호를 한 번 더 입력해주세요."></Input>
        </PassconWrap>
        <Link to="/register/detail">
          <LandingButton isMini={true}>다음으로</LandingButton>
        </Link>
      </Wrap>
    </>
  );
}
// 3개를 감싸는 wrqp, 각각의 wrap

const WrapIn = styled.main`
  display: flex;
  flex-direction: row;
`;
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
const IdWrap = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 5rem;
  ${theme("fonts.textH3")}
  ${theme("neons.textNeonGold")};
`;

const PassWrap = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 5rem;
  ${theme("fonts.textH3")}
  ${theme("neons.textNeonGold")};
`;

const PassconWrap = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 3rem;
  ${theme("fonts.textH3")}
  ${theme("neons.textNeonGold")};
`;

const Input = styled.input`
  width: 20rem;
  border-radius: 2rem;
  ${theme("fonts.textH2")} ${theme("neons.boxNeonGold")};
`;

const LandingButton = styled.span`
  cursor: pointer;
  border-bottom: 0.1rem solid ${theme("colors.mainBlack")};
  padding: 2rem 3.5rem;
  color: ${theme("colors.mainWhite")};
  ${theme("neons.textNeonGold")}
  ${theme("fonts.textH3")}

  &:hover {
    color: ${theme("colors.mainPoint")};
    border-color: ${theme("colors.mainPoint")};
  }
`;
