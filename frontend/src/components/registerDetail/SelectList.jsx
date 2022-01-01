import styled from "styled-components";
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
