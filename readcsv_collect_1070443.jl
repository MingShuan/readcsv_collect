using CSV
using DataFrames
using PrettyTables
csvfile = CSV.read("C:\\homework\\機器學習\\第三周\\data_with_classes.csv",DataFrame)
    global matclass1=[]
    global matclass2=[]
    global matclass3=[]
for row in eachrow(csvfile)
    global matclass1,matclass2,matclass3
    data=Vector(row)
    # print(data)
    index=Int(data[6])
    if index == 1
        push!(matclass1, data[1:5])
    elseif index == 2
        push!(matclass2, data[1:5])
    else
        push!(matclass3, data[1:5])
    end
end
matclass1=transpose(hcat(matclass1...))
matclass2=transpose(hcat(matclass2...))
matclass3=transpose(hcat(matclass3...))
pretty_table(matclass1)
pretty_table(matclass2)
pretty_table(matclass3)





