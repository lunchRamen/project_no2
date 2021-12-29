import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import { StListWrapper } from "./Header";

export default function CommonNav() {
  const navigate = useNavigate();

  const NAVS = [
    { id: 0, navText: "나의 콘텐츠 유형 분석 결과", navigate: () => navigate("contents") },
    { id: 1, navText: "소극장 들어가기", navigate: () => navigate("theaterList") },
    { id: 2, navText: "팀 소개", navigate: () => navigate("/") },
  ];

  return (
    <StWrapper>
      {NAVS.map((nav) => (
        <span key={`nav-${nav.id}`} onClick={nav.navigate}>
          {nav.navText}
        </span>
      ))}
    </StWrapper>
  );
}

const StWrapper = styled(StListWrapper)`
  justify-content: space-between;
  width: 95rem;
`;
