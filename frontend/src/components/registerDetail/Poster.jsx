import styled from "styled-components";
import { theme } from "styled-tools";

export default function Poster({ imgSrc }) {
  return (
    <StWrapper>
      <StTitle>PosterList</StTitle>
      <StPoster src={imgSrc} alt="poster01" />
    </StWrapper>
  );
}

const StWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 20rem;
  height: 33.5rem;
  ${theme("fonts.textP")}
  ${theme("neons.textNeonGold")}

  &:hover {
    color: ${theme("colors.mainPoint")};

    & > img {
      border-color: ${theme("colors.mainPoint")};
      ${theme("neons.boxNeonGold")}
    }
  }
`;

const StTitle = styled.span`
  margin-bottom: 1.5rem;
  width: 100%;
  text-align: center;
`;

const StPoster = styled.img`
  border: 0.1rem solid ${theme("colors.mainBlack")};
  width: 20rem;
  height: 30rem;
`;
