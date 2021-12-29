import React from "react";
import styled from "styled-components";
import { logo, footer } from "../assets/images";
import { theme } from "styled-tools";
import { Button } from "../components";

export default function Landing() {
  return (
    <>
      <Wrap>
        <LandingPage>
          <img src={logo} />
          <p>코로나로 지친 당신을 위한 비대면 극장 식스맨입니다.</p>
        </LandingPage>

        <LandingButton>
          <Button isMini={true}>로그인</Button>
          <Button isMini={true}>회원가입</Button>
        </LandingButton>
      </Wrap>
      <img src={footer} />
    </>
  );
}
const Wrap = styled.div`
  text-align: center;
  margin-top: 25px;
  margin-right: 15%;
  margin-bottom: 20px;
  margin-left: 15%;
`;
const LandingPage = styled.div`
  margin: 10rem, 10rem, 10rem, 10rem;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};
`;

const LandingButton = styled.div`
  margin: 10rem 50rem 10rem 50rem;
  display: flex;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};
`;
