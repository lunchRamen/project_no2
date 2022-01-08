/* eslint-disable prettier/prettier */
import styled from "styled-components";
import { theme } from "styled-tools";
import { Chart } from "../components";
export default function Contents() {
  return (
      <Wrap>
        <LandingPage>안냥하세여</LandingPage>
      <ChartWrap>
        <Chart></Chart>
        <Chart></Chart>
        <Chart></Chart>
      </ChartWrap>
      </Wrap>
  );
}
// background-image: url(${footer});
const Wrap = styled.main`
  // display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 100vw;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 38rem;
    height: 19rem;
  }
`;

const ChartWrap = styled.div`
  // display: flex;
  // flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  
  width: 50vw;
  height: 40vh;
  ${theme("fonts.textH2")}
  ${theme("neons.textNeonGold")};

  & > img {
    width: 38rem;
    height: 19rem;
  }
`;
const LandingPage = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4rem;
`;

// const ButtonWrapper = styled.div`
//   display: flex;
//   justify-content: space-between;
//   margin-bottom: 10rem;
//   width: 87rem;
//   ${theme("fonts.textH2")}
//   ${theme("neons.textNeonGold")};
// `;

// const LandingButton = styled.span`
//   cursor: pointer;
//   border-bottom: 0.1rem solid ${theme("colors.mainBlack")};
//   padding: 2rem 3.5rem;
//   color: ${theme("colors.mainWhite")};
//   ${theme("neons.textNeonGold")}

//   &:hover {
//     color: ${theme("colors.mainPoint")};
//     border-color: ${theme("colors.mainPoint")};
//   }
// `;
