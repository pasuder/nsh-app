package main;

public interface Compute<InputType, OutputType> {

    OutputType compute(InputType value);
}
