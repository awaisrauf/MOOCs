const Header = (props) => {
    return(
        <>
            <h1> {props.course} </h1>
        </>
    )
}

const Part = ({part}) => {
    return (
        <>
        <p>{part.name} {part.exercises}</p> 
        </>
    )
}

const Content = ({parts}) => {
    return(
        <>
            <Part part={parts[0]}/>
            <Part part={parts[1]}/>
            <Part part={parts[2]}/>
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
    const part1 = {
        name: 'Fundamentals of React',
        exercises: 10
    }
    const part2 = {
        name: 'Using props to pass data',
        exercises: 7
    }
    const part3 = {
        name: 'State of a component',
        exercises: 14
    }
    const parts = [part1, part2, part3]

    return (
        <div>
            <Header course={course} />
            <Content parts={parts}/>
            <Total total={part1.exercises+part2.exercises+part3.exercises}/>
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