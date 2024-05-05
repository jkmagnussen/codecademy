Daily Buzz
In this project, you’ll use the commands you just learned to navigate through the files and directories of Daily Buzz, a national newspaper.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

1. Print the working directory.
   pwd
   /home/ccuser/workspace/daily-buzz

2. List all files and directories in the current working directory
   ls
   culture health national technology

3. With one command, change directories to the national/politics/ directory.
   cd national/politics/

4. List all files and directories in the working politics/ directory.
   ls
   policy

5. In the politics/ directory, create a directory called elections/.
   mkdir elections

6. Change directories into the elections/ directory.
   cd elections

7. In the elections/ directory, make two files candidates.txt and issues.txt
   touch candidates.txt issues.txt
   $ ls
   candidates.txt issues.txt

8. Change directories three levels up to the daily-buzz/ directory, and print the working directory.
   cd ../..
   cd ..
   pwd
   /home/ccuser/workspace/daily-buzz

9. In the daily-buzz/ directory, make a directory called business/ and change directories into the business/ directory.
   mkdir business
   $ cd business

10. List all files and directories in the business/ directory
    ls

11. From the business/ directory, make a directory called startups/ and change directories into the startups/ directory.
    mkdir startups
    cd startups

12. Change directories one level up back to the business/ directory. From the business/ directory, make a directory that is a child of startups/, called disruptors/.

pwd
/home/ccuser/workspace/daily-buzz/business/startups
pwd
/home/ccuser/workspace/daily-buzz/business
mkdir startups/disruptors/

13. From the business/ directory, make three files in the disruptors/ directory. The files should be called tech.txt design.txt and education.txt.
    pwd
    /home/ccuser/workspace/daily-buzz/business
    ls
    startups
    touch startups/disruptors/tech.txt
    touch startups/disruptors/design.txt
    touch startups/disruptors/education.txt
    cd cd startups/disruptors
    ls
    design.txt education.txt tech.txt

14. Change directories one level up to the daily-buzz/ directory and print the working directory.

pwd
/home/ccuser/workspace/daily-buzz
