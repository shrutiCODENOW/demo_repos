import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ThemeProvider } from 'styled-components';
import GlobalStyles from './GlobalStyles';
import MovieList from './MovieList'; // Movie list component
import MovieDetails from './MovieDetails'; // Movie details component
import NavigationBar from './NavigationBar';

// Create Query Client
const queryClient = new QueryClient();
const theme={
  primary:"007bff",
  cardBg:"#fff",
  text:'#333',
  inputBorder:"#ccc",
  
  primaryHover:"0056b3",
  background:"#f4f4f4",
  navBg:"#283747 ",
  navText:"white"
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
      <Router>
        <NavigationBar/>
        <div>
          

          {/* Define Routes */}
          <Routes>
            {/* Default route for Movie List */}
            <Route path="/" element={<MovieList />} />

            {/* Dynamic route for Movie Details */}
            <Route path="/movie/:id" element={<MovieDetails />} />
          </Routes>
        </div>
      </Router>
      </ThemeProvider>
    </QueryClientProvider>
    
  );
}

export default App;
