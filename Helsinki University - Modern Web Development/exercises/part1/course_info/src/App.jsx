const Header = (props) => {
    return(
        <>
            <h1> {props.course} </h1>
        </>
    )
}

const Part = ({part, exercises}) => {
    return (
        <>
        <p>{part} {exercises}</p> 
        </>
    )
}

const Content = ({parts, exercises}) => {
    return(
        <>
            <Part part={parts[0]} exercises={exercises[0]}/>
            <Part part={parts[1]} exercises={exercises[1]}/>
            <Part part={parts[2]} exercises={exercises[2]}/>
        </>
    )
}

const Total = ({total}) => {
    return(
        <>
            <p> Total number of courses {total} </p>
        </>
    )
}

const App = () => {
    const course = 'Half Stack application developement'
    const part1 = 'Fundamentals of React'
    const exercises1 = 10
    const part2 = 'Using props to pass data'
    const exercises2 = 7
    const part3 = 'State of a component'
    const exercises3 = 14

    let parts = [part1,part2,part3]
    let exercises = [exercises1,exercises2,exercises3]

    return (
        <div>
            <Header course={course} />
            <Content parts={parts} exercises={exercises} />
            <Total total={exercises1+exercises2+exercises3}/>
        </div>
    )

}

export default App
// const App = () => {
//   const course = 'Half Stack application developement'
//   const part1 = 'Fundamentals of React'
//   const exercises1 = 10
//   const part2 = 'Using props to pass data'
//   const exercises2 = 7
//   const part3 = 'State of a component'
//   const exercises3 = 14

// return (
//   <div>
//     <h1> {course} </h1>
//     <p>
//       {part1} {exercises1}
//     </p>
//     <p>
//       {part2} {exercises2}
//     </p>
//     <p>
//       {part3} {exercises3}
//     </p>

//     <p> Number of exercises {exercises1+exercises2+exercises3}</p>
//   </div>
// )
// }