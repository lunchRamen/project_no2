import React, { useState } from "react";
import { Button, PosterList } from "../components";
import styled from "styled-components";
import { theme } from "styled-tools";
import { useNavigate } from "react-router-dom";
import Fade from "react-reveal/Fade";

export default function RegisterStep3() {
  const navigate = useNavigate();
  const [genre, setGenre] = useState([1, 2, 3, 4]);

  return (
    <Wrapper>
      <Fade>
        <Intro>다음 중 가장 좋아하는 또는 재밌을 것 같은 영화 6가지를 선택해주세요!</Intro>
        <PosterList genre={genre} setGenre={setGenre} />
        <Button isMini={false} onClick={() => navigate("/register/done")}>
          로그인
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
