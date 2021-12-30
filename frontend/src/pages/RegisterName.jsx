// import { Button } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { Link } from "react-router-dom";
export default function RegisterName() {
  return (
    <>
      <Wrap>
        <p>시작하기 전, 이름을 설정해주세요!</p>
        <p>실명이어도 좋고, 닉네임이어도 무관합니다.</p>
        <InputWrap>
          <Input type="text" name="name" style={{ color: "white" }}></Input>
          <br />
          <Link to="/register/id">
            <LandingButton isMini={true}>다음</LandingButton>
          </Link>
        </InputWrap>
      </Wrap>
    </>
  );
}

const Wrap = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 70vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};
`;
const InputWrap = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 7rem;
  width: 40rem;
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

  &:hover {
    color: ${theme("colors.mainPoint")};
    border-color: ${theme("colors.mainPoint")};
  }
`;
