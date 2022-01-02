import styled from "styled-components";
import { theme } from "styled-tools";
import { BasicSelect, DetailSelect } from "..";

export default function SelectList({ data }) {
  return (
    <StWrapper>
      <BasicSelect />
      <DetailSelect data={data} />
    </StWrapper>
  );
}
const StWrapper = styled.section`
  display: flex;
  flex-direction: column;
`;

export const Select = styled.select`
  border: 0.1rem solid ${theme("colors.mainWhite")};
  background-color: black;
  width: ${({ selectWidth }) => selectWidth};
  height: 4rem;
  color: white;
  font-family: NotoSerif;
  ${theme("fonts.textP")}
  ${theme("neons.boxNeonGold")}
`;
